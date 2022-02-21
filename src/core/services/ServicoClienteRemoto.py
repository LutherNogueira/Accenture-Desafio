from distutils import core
from typing import Iterable
from src.core.models.Cliente import Cliente
from src.core.services.ServicoCliente import ServicoClienteLocal

class ServicoClienteRemoto(ServicoClienteLocal):
    def __init__(self,conexao,tabela='CLIENTES'):
        self.conexao = conexao
        self.tabela = tabela
    
    def createTable(self,cliente:Cliente):
        cursor = self.conexao.cursor()
        cursor.execute(
            f'''
            CREATE TABLE {self.tabela}(
                ID INT PRIMARY KEY,
                NOME VARCHAR(100),
                EMAIL VARCHAR(100),
                DATA_CADASTRO DATETIMEOFFSET,
                TELEFONE VARCHAR(20)
            )''',
            [cliente.id,cliente.nome,cliente.email,cliente.data_cadastro,cliente.telefone]
        )
        cursor.close()

    def insert(self,cliente:Cliente):
        cursor = self.conexao.cursor()
        cursor.execute(
            f'''
            INSERT INTO {self.tabela}(ID, NOME, EMAIL, DATA_CADASTRO, TELEFONE)
            VALUES(?,?,?,?,?)
            ''',
            [cliente.id,cliente.nome,cliente.email,cliente.data_cadastro,cliente.telefone]
        )
        cursor.close()

    def escrever(self, clientes: Iterable[Cliente]):
        for cliente in clientes:
            self.insert(cliente)
        self.conexao.commit()