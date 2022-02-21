from typing import List
from models.Transacao import Transacao
from pandas import DataFrame
from services.ServicoODBC import ServiceODBC
from pyodbc import Error


class ServiceTransacao:

    @staticmethod
    def cadastrar(listaTransacao: DataFrame, clientes):
        try:
            transacoes = []

            for index, linha in listaTransacao.iterrows:

                cliente = [
                    cliente for cliente in clientes if cliente.id == linha["cliente_id"]]

                transacao = Transacao(
                    linha["id"],
                    cliente,
                    linha["valor"],
                    linha["data"]
                )

                transacoes.append(transacao)

            return transacoes
        except OSError as err:
            print("Erro de Sistema Operacional: {0}".format(err))
        except ValueError:
            print("Não foi possível fazer a conversão de tipo")
        except BaseException as err:
            print(f"Erro inesperado {err=}, {type(err)=}")

    @staticmethod
    def criarTabelas():

        try:
            if ServiceODBC.checkIfTableExists("TRANSACOES"):
                print('Tabela TRANSACOES já existe! Tabela não foi criada')
            else:

                comando_sql = '''
                    CREATE TABLE TRANSACOES(
                        ID INT PRIMARY KEY NOT NULL,
                        CLIENTE_ID INT FOREIGN KEY REFERENCES CLIENES(ID) NOT NULL,
                        VALOR FLOAT,
                        DATA DATETIMEOFFSET

                    )
                '''
                cursor, conn = ServiceODBC.openConnection()
                
                cursor.execute(comando_sql)
                conn.commit()

        except Error as e:
            print(f'Falha ao criar tabela CLIENTES:{str(e)}')
        finally:
            cursor.close()
            conn.close()

    @staticmethod
    def inserirDB(listaTransacao:List[Transacao]):
        try:
            
            comando_sql = '''
                INSERT INTO TRANSACAO (ID, CLIENTE_ID, VALOR, DATA)
                VALUES(?,?,?,?)
            '''
            cursor, conn = ServiceODBC.openConnection()

            for transacao in listaTransacao:
                values = (transacao.id, transacao.id_cliente.id, transacao.valor, transacao.data)
                cursor.execute(comando_sql, values)
            conn.commit()

        except Error as e:
            print(f'Falha ao gravar registros na tabela CLIENTES:{str(e)}')
        finally:
            cursor.close()
            conn.close()
