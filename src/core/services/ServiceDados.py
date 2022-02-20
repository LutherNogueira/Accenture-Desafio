from src.core.services.ServicePandas import ServicePandas
from src.core.services.ServiceCliente import ServiceCliente
from src.core.services.ServiceTransacao import ServiceTransacao
from src.core.services.ServiceODBC import ServiceODBC
from pyodbc import Error

import pandas as pd


class ServiceDados:

    @staticmethod
    def carregarDoCSV():

       # transaction_in = ServicePandas.readDataTransationIn(1, 1)
        #transaction_out = ServicePandas.readDataTransationOut(1, 1)
        clientes = ServicePandas.readDataCliente()

        #transaction = pd.concat([transation_in, transation_out])
        transacoes = ServicePandas.readDataTransation()

        clientes = ServiceCliente.cadastrar(clientes)
        transacoes = ServiceTransacao.cadastrar(transacoes, clientes)

        dict_tabelas = {}

        dict_tabelas["clientes"] = clientes
        dict_tabelas["transacoes"] = transacoes

        return dict_tabelas

    @staticmethod
    def apagarDadosCarregados(dict_tabelas):
        dict_tabelas['clientes'] = []
        dict_tabelas['transacoes'] = []

        return dict_tabelas

    @staticmethod
    def Sumarizar(dict_tabelas):
        print(
            f'Temos { len(dict_tabelas["clientes"]) } registros na tabela clientes')
        print(
            f'Temos { len(dict_tabelas["transaction"]) } registros na tabela transações')

    @staticmethod
    def criarTabelasDB():
        ServiceCliente.criarTabelas()
        ServiceTransacao.criarTabelas()

    @staticmethod
    def dropAllTables():
        ServiceODBC.deleteAllTables()

    @staticmethod
    def inserirNasTabelasDB(dict_tabelas):

        ServiceCliente.inserirDB(dict_tabelas['clientes'])
        ServiceTransacao.inserirDB(dict_tabelas['transacoes'])

    @staticmethod
    def SumarizarDB():
        tabelas = ['CLIENTES', 'TRANSACOES']

        try:
            cursor, conn = ServiceODBC.openConection()

            for item in tabelas:
                if ServiceODBC.checkIfTableExists(item):
                    comando_sql = "SELECT COUNT(ID) QTD FROM {item} "
                    cursor.execute(comando_sql)

                    linha = cursor.fetchone()

                    print(f'Na tabela {item} temos {linha.QTD} registros')
                else:
                    print("Tabela {item} não existe no banco de dados")

        except Error as e:
            print(f"Erro ao sumarizar dados do banco de dados : {str(e)}")
        except OSError as err:
            print("Erro de Sistema Operacional: {0}".format(err))
        except ValueError:
            print("Não foi possível fazer a conversão de tipo")
        except BaseException as err:
            print(f"Erro inesperado {err=}, {type(err)=}")
