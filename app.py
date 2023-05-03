from flask_openapi3 import OpenAPI, Info, Tag
from flask import redirect, jsonify 
from flask_cors import CORS
from model import *
from schemas import *
from sqlalchemy.orm.session import close_all_sessions

info = Info(title = "Minha API", version = "1.0.0")
app = OpenAPI(__name__,info=info)
CORS(app)

#-------------------------------
#Definindo minhas Rotas
#-------------------------------

documentacao_tag = Tag(name = "Documentação", description = "Redireciona para a documentação")
estoque_tag = Tag(name = "Estoque", description = "Funções para criar ou alterar itens do estoque")
carrinho_tag = Tag(name = "Carrinho", description = "Funções para inserir ou remover itens do carrinho")

@app.get('/', tags = [documentacao_tag])
def home():
    return redirect('/openapi')

@app.get('/estoque', tags = [estoque_tag])
def getEstoque():
    """
    Lista todos os dados da tabela Estoque armazenados no banco de dados (BD)
    """
    session = Session()
    produtos = session.query(Estoque).all()
    return jsonify({'produtos':[apresentaEstoque(produto) for produto in produtos]})


@app.put('/remove_estoque', tags = [estoque_tag])
def removeEstoque(form:putEstoqueSchema):
    """
    Recebe após o fechamento do carrinho (compra): IDs dos produtos, tamanhos e quantidades compradas para abater da quantidade de itens disponíveis em estoque
    """
    print (form.quantidade)
    session = Session()
    produto = session.query(Estoque).filter(Estoque.id == form.id).first()
    if form.tamanho == "G":
        print("Entrou no G")
        produto.qtd_g -= form.quantidade
    elif form.tamanho == "M":  
        print("Entrou no M")
        produto.qtd_m -= form.quantidade
    elif form.tamanho == "P":  
        print("Entrou no P")
        produto.qtd_p -= form.quantidade
    else:
        return "Tamanho informado não existe!"
    
    session.commit()
    return "Produto removido do estoque!"

@app.put('/adiciona_estoque', tags = [estoque_tag])
def adicionaEstoque(form:putEstoqueSchema):
    """
    Recebe ID do item, qtd e tamanho e incrementa a quantidade de peças em estoque no tamanho informado  
    """
    #print (form.quantidade)
    session = Session()
    produto = session.query(Estoque).filter(Estoque.id == form.id).first()
    if form.tamanho == "G":
        #print("Entrou no G")
        produto.qtd_g += form.quantidade
    elif form.tamanho == "M":  
        #print("Entrou no M")
        produto.qtd_m += form.quantidade
    elif form.tamanho == "P":  
        #print("Entrou no P")
        produto.qtd_p += form.quantidade
    else:
        return "Tamanho informado não existe!"
    session.commit()
    return "Produto adicionado no estoque!"

@app.get('/carrinho', tags = [carrinho_tag])
def getCarrinho():
    """
    Lista todos os produtos da tabela Carrinho armazenados no banco de dados (BD)
    """
    session = Session()
    produtos = session.query(Carrinho).all()
    return jsonify({'produtos':[apresentaCarrinho(produto) for produto in produtos]})

@app.post('/carrinho', tags = [carrinho_tag])
def postCarrinho(form:CarrinhoSchema):
    """
    Insere produto selecionado pelo usuário no carrinho de compras
    """
    carrinho = Carrinho(
        id_produto = form.id_produto,
        nome = form.nome,
        preco = form.preco,
        tamanho = form.tamanho,
        quantidade = form.qtd
    )

    session = Session()
    session.add(carrinho)
    session.commit() #salva no banco
    return "Produto adicionado!"
    
@app.delete('/carrinho', tags = [carrinho_tag])
def delCarrinho(form:idCarrinhoSchema):
    """
    Recebe ID do produto e remove do carrinho de compras
    """
    session = Session()
    session.query(Carrinho).filter(Carrinho.id == form.id).delete()
    session.commit()
    return "Produto removido do carrinho!"
