from typing import Iterable,Callable
from core.models.Cliente import Cliente
from core.services.ServicoODBC import ServiceODBC
import csv
import glob
import pyodbc

class ServicoCliente():
    def ler(self) -> Iterable[Cliente]:
        raise NotImplementedError()

    def escrever(self,clientes:Iterable[Cliente]):
        raise NotImplementedError()

class ServicoClientePandas(ServicoCliente):
    def __init__(self,provedorArquivos:Callable[[],Iterable[str]]):#tipo função(callable) que retornara um (iterable) strings
        self.provedorArquivos = provedorArquivos

    def ler(self):
        for arquivo in self.provedorArquivos():
            with open(arquivo,'r',encoding='utf-8') as dado:
                for linha in csv.DictReader(dado,delimiter=';',quoting=csv.QUOTE_NONE):
                    try:
                        cliente=Cliente.dadoBruto(linha)
                        yield cliente
                    except Exception as erro:
                        raise Exception(f'Erro no arquivo => {arquivo}',erro)

class ServicoClienteBD(ServicoCliente):
    def __init__(self,conexao,tabela='clientes'):
        self.conexao = conexao
        self.tabela = tabela
    
    def createTable(self,cliente:Cliente):
        cursor = self.conexao.cursor()
        cursor.execute(
            f'''
            create table clientes(
            id int primary key,
            nome text,
            email text,
            data_cadastro datetime,
            telefone text
            )
            ''',
            [cliente.id,cliente.nome,cliente.email,cliente.data_cadastro,cliente.telefone]
        )
        cursor.close()

    def insert(self,cliente:Cliente):
        cursor = self.conexao.cursor()
        cursor.execute(
            f'''
            INSERT INTO {self.tabela}(id,nome,email,data_cadastro,telefone)
            VALUES(?,?,?,?,?)
            ''',
            [cliente.id,cliente.nome,cliente.email,cliente.data_cadastro,cliente.telefone]
        )
        cursor.close()

    def escrever(self, clientes: Iterable[Cliente]):
        for cliente in clientes:
            self.insert(cliente)
        self.conexao.commit()

def migracao(de:ServicoCliente,para:ServicoCliente):
    clientes = de.ler()
    para.escrever(clientes)


if __name__ == '__main__':
    servicoPandas = ServicoClientePandas(
        lambda:glob.glob('D:\Accenture\Accenture-Grupo-Ada\src\db\clients-001.csv')
    )
    servicoBanco = ServicoClienteBD(ServiceODBC.justConection())
    migracao(servicoPandas,servicoBanco)