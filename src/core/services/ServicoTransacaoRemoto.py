from typing import Iterable
from models.Transacao import Transacao
from services.ServicoTransacaoLocal import ServicoTransacaoLocal
from services.ServicoODBC import ServiceODBC

class ServicoTransacaoRemoto(ServicoTransacaoLocal):
    def __init__(self,conexao,tabela='TRANSACOES'):
        self.conexao = conexao
        self.tabela = tabela
    
    def createTable(self):
        if ServiceODBC.checkIfTableExists("TRANSACOES"):
                print('Tabela TRANSACOES já existe! Tabela não foi criada')
        else:
            cursor = self.conexao.cursor()
            cursor.execute(
                f'''
                CREATE TABLE {self.tabela}(
                            ID INT PRIMARY KEY NOT NULL,
                            CLIENTE_ID INT NOT NULL,
                            VALOR FLOAT,
                            DATA DATETIMEOFFSET
                )'''
            )
            self.conexao.commit()
            cursor.close()

    def insert(self,transacao:Transacao):
        cursor = self.conexao.cursor()
        cursor.execute(
            f'''
            INSERT INTO {self.tabela} (ID, CLIENTE_ID, VALOR, DATA)
                VALUES(?,?,?,?)
            ''',
            [transacao.id, transacao.cliente_id, transacao.valor, transacao.data]
        )
        cursor.close()

    def escrever(self, transacoes: Iterable[Transacao]):
        for transacao in transacoes:
            self.insert(transacao)
        self.conexao.commit()