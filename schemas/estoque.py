from pydantic import BaseModel
from model import *

class EstoqueSchema(BaseModel):
    nome: str
    preco: float
    qtd_g: int
    qtd_m: int
    qtd_p: int

class putEstoqueSchema(BaseModel):
    id: int
    quantidade: int
    tamanho: str

def apresentaEstoque(estoque: Estoque):
    return {
        'id': estoque.id,
        'nome': estoque.nome,
        'preco': estoque.preco,
        'qtd_g': estoque.qtd_g,
        'qtd_m': estoque.qtd_m,
        'qtd_p': estoque.qtd_p
    }



