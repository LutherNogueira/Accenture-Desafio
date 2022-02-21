from typing import Iterable
from models.Cliente import Cliente
from services.ServicoClienteLocal import ServicoClienteLocal
from pyodbc import Error

class ServicoClienteRemoto(ServicoClienteLocal):
    def __init__(self,conexao,tabela='CLIENTES'):
        self.conexao = conexao
        self.tabela = tabela
    
    def createTable(self):
        try: 

            cursor = self.conexao.cursor()
            cursor.execute(
                f'''
                CREATE TABLE {self.tabela}(
                    ID INT PRIMARY KEY,
                    NOME VARCHAR(100),
                    EMAIL VARCHAR(100),
                    DATA_CADASTRO DATETIMEOFFSET,
                    TELEFONE VARCHAR(20)
                )'''
            )
            self.conexao.commit()
            cursor.close()
            print(f"Tabela {self.tabela} criada com sucesso\n")
        except Error as e:
            print(f"Erro ao criar tabela {self.tabela } no banco de dados : {str(e)}")
        except OSError as err:
            print("Erro de Sistema Operacional: {0}".format(err))
        except ValueError:
            print("Não foi possível fazer a conversão de tipo")
        except BaseException as err:
            print(f"Erro inesperado {err=}, {type(err)=}")

    def insert(self,cliente:Cliente):
        try:
            cursor = self.conexao.cursor()
            cursor.execute(
                f'''
                INSERT INTO {self.tabela}(ID, NOME, EMAIL, DATA_CADASTRO, TELEFONE)
                VALUES(?,?,?,?,?)
                ''',
                [cliente.id,cliente.nome,cliente.email,cliente.data_cadastro,cliente.telefone]
            )
            cursor.close()
            print("Cliente: {cliente} inserido com sucesso no banco de dados")
        except Error as e:
            print(f"Erro ao inserir {cliente} no banco de dados : {str(e)}")
        except OSError as err:
            print("Erro de Sistema Operacional: {0}".format(err))
        except ValueError:
            print("Não foi possível fazer a conversão de tipo")
        except BaseException as err:
            print(f"Erro inesperado {err=}, {type(err)=}")

    def escrever(self, clientes: Iterable[Cliente]):
        for cliente in clientes:
            self.insert(cliente)
        self.conexao.commit()