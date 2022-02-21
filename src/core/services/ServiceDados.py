from glob import glob
from services.ServicoClienteLocal import ServicoClienteLocal
from services.ServiceTransacao import ServiceTransacao
from services.ServiceODBC import ServiceODBC
from services.ServicoClienteRemoto import ServicoClienteRemoto
from services.ServicePandas import ServicePandas
from services.ServicoCliente import ServicoCliente
from services.ServicoTransacao import ServicoTransacao
from services.ServicoTransacaoLocal import ServicoTransacaoLocal
from services.ServicoTransacaoRemoto import ServicoTransacaoRemoto

from pyodbc import Error

import pandas as pd


class ServiceDados:

    @staticmethod
    def carregarDoCSV():

        # clientes_csv = ServicePandas.readDataCliente()
        # cliente_local = ServicoClienteLocal(clientes_csv)
        
        # cliente_remoto = ServicoClienteRemoto(ServiceODBC.openConnection())
        # ServiceDados.migracaoCliente(cliente_local,cliente_remoto)

        transacao_csv = ServicePandas.readDataTransacao()
        transacao_local = ServicoTransacaoLocal(transacao_csv)
        transacao_remoto = ServicoTransacaoRemoto(ServiceODBC.openConnection())
        transacao_remoto.createTable()
        ServiceDados.migracaoTransacao(transacao_local,transacao_remoto)
           
    def migracaoCliente(de:ServicoCliente,para:ServicoCliente):
        clientes = de.ler()
        para.escrever(clientes)
    
    def migracaoTransacao(de:ServicoTransacao,para:ServicoTransacao):
        transacoes = de.ler()
        para.escrever(transacoes)

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
            conn = ServiceODBC.openConnection()

            for item in tabelas:
                if ServiceODBC.checkIfTableExists(item):
                    comando_sql = "SELECT id as QTD FROM {item};"
                    conn.cursor().execute(comando_sql)

                    linha = conn.cursor().fetchone()

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
