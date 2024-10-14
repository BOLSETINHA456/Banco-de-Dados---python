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

class Aluno(Base):
    __tablename__ = "alunos"

    # Definindo campos da tabela.
    R_A = Column("R.A", Integer, primary_key=True, autoincrement=True)
    nome = Column("nome", String)
    sobrenome = Column("sobrenome", String)
    email = Column("email", String)
    senha = Column("senha", String)

    # Definindo atributos da classe.
    def __init__(self, nome: str, sobrenome: str, email: str, senha: str):
        self.nome = nome
        self.sobrenome = sobrenome
        self.email = email
        self.senha = senha

# Criando tabela no banco de dados.
Base.metadata.create_all(bind=MEU_BANCO)

# CRUD.
# Create - insert - salvar.
os.system("cls || clear")
print ("Solicitando dados para o aluno.")
inserir_nome = input("Digite seu nome: ")
inserir_sobrenome = input("Digite seu sobrenome: ")
inserir_email = input("Digite seu email: ")
inserir_senha = input("Digite seu senha: ")

aluno = Aluno(nome=inserir_nome, sobrenome=inserir_sobrenome, email=inserir_email, senha=inserir_senha)
session.add(aluno)
session.commit()

# Read - Select - Consulta
print("\nExibindo dados de todos os Alunos.")
lista_aluno = session.query(Aluno).all()

for aluno in lista_aluno:
    print(f"{aluno.R_A} - {aluno.nome} - {aluno.sobrenome} - {aluno.email} - {aluno.senha}")

# U - Update - UPDATE - Atualizar
print ("\nAtualizando dados do aluno.")
email_aluno = input("Digite o e-mail do aluno que será atualizado: ")

aluno = session.query(Aluno).filter_by(email_aluno).first()

if aluno:
    aluno.nome = input("Digite seu nome: ")
    aluno.email = input("Digite seu email: ")
    aluno.senha = input("Digite seu senha: ")
    
    session.commit()
else: 
    print ("Aluno não encontrado")

# R - Read - SELECT - Consulta
print("\nExibindo dados de todos os Alunos.")

for aluno in lista_aluno:
    print(f"{aluno.R_A} - {aluno.nome} - {aluno.sobrenome} - {aluno.email} - {aluno.senha}")

# D - Delete - DELETE - Excluir
print ("\nExcluindo ")
email_aluno = input("Digite o e-mail do Aluno que será excluido: ")

aluno = session.query(Aluno).filter_by(email = email_aluno).first()

if aluno:
    session.delete(aluno)
    session.commit()
    print(f"Aluno {aluno.nome} excluido com sucesso!")
else:
    print("Aluno não encontrado.")

# R - Read - SELECT - Consulta
print("\nExibindo dados de todos os Alunos.")
lista_aluno = session.query(Aluno).all()

for aluno in lista_aluno:
    print(f"{aluno.R_A} - {aluno.nome} - {aluno.sobrenome} - {aluno.email} - {aluno.senha}")

# R - Read - SELECT - Consulta
print("Consultando os dados de apenas um Aluno")
email_aluno = input("Digite o e-mail do Aluno: ")

aluno = session.query(Aluno).filter_by(email = email_aluno).first()

if aluno:
    print(f"{aluno.R_A} - {aluno.nome} - {aluno.sobrenome} - {aluno.email} - {aluno.senha}")
else:
    print("Aluno não encontrado.")

# Fechando conexão
session.close()