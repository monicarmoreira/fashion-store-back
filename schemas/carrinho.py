from pydantic import BaseModel
from model import *

class CarrinhoSchema(BaseModel):
    id_produto: int
    nome: str
    tamanho: str
    preco: float
    qtd: int

class idCarrinhoSchema(BaseModel):
    id: int
    
def apresentaCarrinho(carrinho: Carrinho):
    return{
        "id": carrinho.id,
        "id_produto": carrinho.id_produto,
        "nome": carrinho.nome,
        "preco": carrinho.preco,
        "tamanho": carrinho.tamanho,
        "qtd": carrinho.quantidade
    }