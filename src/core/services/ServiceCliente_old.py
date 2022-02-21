from typing import List
from pandas import DataFrame
from models.Cliente import Cliente
from services.ServiceODBC import ServiceODBC
from pyodbc import Error

class ServiceCliente:
    @staticmethod
    def cadastrar(listaClientes:DataFrame ):
        try:
            clientes=[]
            for index, linha in listaClientes.iterrows:
                cliente = Cliente(
                    linha["id"],
                    linha["nome"],
                    linha["email"],
                    linha["data_cadastro"],
                    linha["telefone"]
                )
                clientes.append(cliente)

            return clientes

        except OSError as err:
            print("Erro de Sistema Operacional: {0}".format(err))
        except ValueError:
            print("Não foi possível fazer a conversão de tipo")
        except BaseException as err:
            print(f"Erro inesperado {err=}, {type(err)=}")

    @staticmethod
    def criarTabelas():

        try:

            if ServiceODBC.checkIfTableExists("CLIENTES"):
                print('Tabela CLIENTES já existe! Tabela não foi criada')
            else:
                comando_sql='''
                        CREATE TABLE CLIENTES(
                            ID INT PRIMARY KEY,
                            NOME VARCHAR(100),
                            EMAIL VARCHAR(100),
                            DATA_CADASTRO DATETIMEOFFSET,
                            TELEFONE VARCHAR(20)
                        )
                '''
                cursor, conn = ServiceODBC.openConection()
                cursor.execute(comando_sql)
                conn.commit()

                print("Tabela CLIENTES criada com sucesso")
        except Error as e:
            print(f'Falha ao criar tabela CLIENTES:{str(e)}')
        finally:
            cursor.close()
            conn.close()

    def inserirDB(listaClientes:List[Cliente]):
        try:
            comando_sql='''
                    INSERT INTO CLIENTES (ID, NOME, EMAIL, DATA_CADASTRO, TELEFONE)
                    VALUES(?,?,?,?,?)
                '''
            for cliente in listaClientes:

                values = (cliente.id, cliente.nome, cliente.email, cliente.data_cadastro, cliente.telefone )

                cursor, conn = ServiceODBC.openConection()
                cursor.execute(comando_sql, values)

            conn.commit()

        except Error as e:
            print(f'Falha ao gravar registros na tabela CLIENTES:{str(e)}')
        finally:
            cursor.close()
            conn.close()


