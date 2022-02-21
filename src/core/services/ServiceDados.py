from glob import glob
from src.core.services.ServicoClienteLocal import ServicoClienteLocal
from src.core.services.ServiceTransacao import ServiceTransacao
from src.core.services.ServiceODBC import ServiceODBC
from src.core.services.ServicoClienteRemoto import ServicoClienteRemoto
from src.core.services.ServicePandas import ServicePandas
from src.core.services.ServicoCliente import ServicoCliente
from pyodbc import Error

import pandas as pd


class ServiceDados:

    @staticmethod
    def carregarDoCSV():

        clientes_csv = ServicePandas.readDataCliente()
        cliente_local = ServicoClienteLocal(clientes_csv)
        
        cliente_remoto = ServicoClienteRemoto(ServiceODBC.justConection())
        ServiceDados.migracao(cliente_local,cliente_remoto)
       

        return dict_tabelas
    
    def migracao(de:ServicoCliente,para:ServicoCliente):
        clientes = de.ler()
        para.escrever(clientes)

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
