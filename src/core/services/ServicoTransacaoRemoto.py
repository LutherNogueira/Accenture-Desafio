from typing import Iterable
from models.Transacao import Transacao
from services.ServicoTransacaoLocal import ServicoTransacaoLocal
from services.ServicoODBC import ServiceODBC
from pyodbc import Error

#servico transacao remoto esta relacionado com o banco de dados --> por isso seu init recebe uma conexao de BD
class ServicoTransacaoRemoto(ServicoTransacaoLocal):
    def __init__(self,conexao,tabela='TRANSACOES'):
        self.conexao = conexao
        self.tabela = tabela
    
    def createTable(self):
        try:

            if ServiceODBC.checkIfTableExists(self.tabela):
                    print(f'Tabela {self.tabela} já existe! Tabela não foi criada')
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
                print(f"Tabela {self.tabela} criada com sucesso")

        except Error as e:
            print(f"Erro ao criar tabela {self.tabela} no banco de dados : {str(e)}")
        except OSError as err:
            print("Erro de Sistema Operacional: {0}".format(err))
        except ValueError:
            print("Não foi possível fazer a conversão de tipo")
        except BaseException as err:
            print(f"Erro inesperado {err=}, {type(err)=}")

    def insert(self,transacao:Transacao):
        
        try:
            cursor = self.conexao.cursor()
            cursor.execute(
                f'''
                INSERT INTO {self.tabela} (ID, CLIENTE_ID, VALOR, DATA)
                    VALUES(?,?,?,?)
                ''',
                [transacao.id, transacao.cliente_id, transacao.valor, transacao.data]
            )
            cursor.close()
            print(f"Transação: {transacao.id} inserido com sucesso no banco de dados")
        except Error as e:
            print(f"Erro ao inserir transacao {transacao} no banco de dados : {str(e)}")
        except OSError as err:
            print("Erro de Sistema Operacional: {0}".format(err))
        except ValueError:
            print("Não foi possível fazer a conversão de tipo")
        except BaseException as err:
            print(f"Erro inesperado {err=}, {type(err)=}")

    def escrever(self, transacoes: Iterable[Transacao]): #Iterable[Transacao] --> é o método ler() do transacao_local(que por ter o yield dentro dele se torna do tipo itereable)
                                                    #e como esse Yield esta guardando nosso transacao, ele é um iterable do tipo transacao
        for transacao in transacoes:            #for esta sendo feito emcima do método ler da objeto transacao_local
            self.insert(transacao)
        self.conexao.commit()