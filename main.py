""" BANCO DE DADOS
    - SQL (LINGUAGEM DE CONSULTA ESTRUTURADA)
    - EXEMPLO:
        - SELECT * FROM CLIENTES;
        - IRÁ CONSULTAR O BD DA TABELA CLIENTES.

        - SGBD:
            - GERENCIAR PERMISSÕES DE ACESSO
            ADMINISTRADOR DE BANCO DE DADOS (DBA)
            - CRIAR CONSULTAS PERSONALIZADAS 
            - SELECT * FROM CLIENTES;
        - ORM: MAPEAMENTO OBJETO RELACIONAL
            - USAR A LINGUAGEM DE PROGRAMAÇÃO MANIPULAR O BANCO DE DADOS
"""
import os
from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.orm import sessionmaker, declarative_base

# Criando banco de dados.
MEU_BANCO = create_engine("sqlite:///meubanco.db")

# Criando conexão com banco de dados.
Session = sessionmaker(bind=MEU_BANCO)
session = Session()

# Criando tabela.

Base = declarative_base()

class Cliente(Base):
    __tablename__ = "clientes"

    # Definindo campos da tabela.
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    nome = Column("nome", String)
    email = Column("email", String)
    senha = Column("senha", String)

    # Definindo atributos da classe.
    def __init__(self, nome: str, email: str, senha: str):
        self.nome = nome
        self.email = email
        self.senha = senha

# Criando tabela no banco de dados.
Base.metadata.create_all(bind=MEU_BANCO)

# CRUD.
# Create - insert - salvar.
os.system("cls || clear")
print ("Solicitando dados para o usuário.")
inserir_nome = input("Digite seu nome: ")
inserir_email = input("Digite seu email: ")
inserir_senha = input("Digite seu senha: ")

cliente = Cliente(nome=inserir_nome, email=inserir_email, senha=inserir_senha)
session.add(cliente)
session.commit()

# Read - Select - Consulta
print("\nExibindo dados de todos os clientes.")
lista_cliente = session.query(Cliente).all()

for cliente in lista_cliente:
    print(f"{cliente.id} - {cliente.nome} - {cliente.email} - {cliente.senha}")

# U - Update - UPDATE - Atualizar
print ("\nAtualizando dados do usuário.")
email_cliente = input("Digite o e-mail do cliente que será atualizado: ")

cliente = session.query(Cliente).filter_by(email_cliente).first()

if cliente:
    cliente.nome = input("Digite seu nome: ")
    cliente.email = input("Digite seu email: ")
    cliente.senha = input("Digite seu senha: ")
    
    session.commit()
else: 
    print ("Cliente não encontrado")

# R - Read - SELECT - Consulta
print("\nExibindo dados de todos os clientes.")

for cliente in lista_cliente:
    print(f"{cliente.id} - {cliente.nome} - {cliente.email} - {cliente.senha}")

# D - Delete - DELETE - Excluir
print ("\nExcluindo ")
email_cliente = input("Digite o e-mail do cliente que será excluido: ")

cliente = session.query(Cliente).filter_by(email = email_cliente).first()

if cliente:
    session.delete(cliente)
    session.commit()
    print(f"cliente {cliente.nome} excluido com sucesso!")
else:
    print("cliente nao encontrado.")

# R - Read - SELECT - Consulta
print("\nExibindo dados de todos os clientes.")
lista_cliente = session.query(Cliente).all()

for cliente in lista_cliente:
    print(f"{cliente.id} - {cliente.nome} - {cliente.email} - {cliente.senha}")

# R - Read - SELECT - Consulta
print("Consultando os dados de apenas um cliente")
email_cliente = input("Digite o e-mail do cliente: ")

cliente = session.query(Cliente).filter_by(email = email_cliente).first()

if cliente:
    print(f"{cliente.id} - {cliente.nome} - {cliente.email} - {cliente.senha}")
else:
    print("Cliente não encontrado.")

# Fechando conexão
session.close()