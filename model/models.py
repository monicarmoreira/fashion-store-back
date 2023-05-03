from sqlalchemy import create_engine, Column, Integer, String, Text, Float
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Estoque(Base):
    __tablename__ = 'estoque'
    id = Column(Integer, primary_key=True)
    nome = Column(String(255))
    preco = Column(Float)
    qtd_g = Column(Integer)
    qtd_m = Column(Integer)
    qtd_p = Column(Integer)

class Carrinho(Base):
    __tablename__ = 'carrinho'
    id = Column(Integer, primary_key=True)
    id_produto = Column(Integer)
    nome = Column(String(255))
    tamanho = Column(String(1))
    preco = Column(Float)
    quantidade = Column(Integer)


