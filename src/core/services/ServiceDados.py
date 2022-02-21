from services.ServicoClienteLocal import ServicoClienteLocal
from services.ServicoODBC import ServiceODBC
from services.ServicoClienteRemoto import ServicoClienteRemoto
from services.ServicoPandas import ServicePandas
from services.ServicoCliente import ServicoCliente
from services.ServicoTransacao import ServicoTransacao
from services.ServicoTransacaoLocal import ServicoTransacaoLocal
from services.ServicoTransacaoRemoto import ServicoTransacaoRemoto

from pyodbc import Error

import pandas as pd


class ServiceDados:

    @staticmethod
    def carregareMigrar():

        clientes_csv = ServicePandas.readDataCliente()
        cliente_local = ServicoClienteLocal(clientes_csv)
        
        transacao_csv = ServicePandas.readDataTransacao()
        transacao_local = ServicoTransacaoLocal(transacao_csv)

        cliente_remoto = ServicoClienteRemoto(ServiceODBC.openConnection())
        ServiceDados.migracaoCliente(cliente_local, cliente_remoto)

        transacao_remoto = ServicoTransacaoRemoto(ServiceODBC.openConnection())
        ServiceDados.migracaoTransacao(transacao_local, transacao_remoto)

           
    def migracaoCliente(de:ServicoCliente,para:ServicoCliente):
        clientes = de.ler()
        para.escrever(clientes)
    
    def migracaoTransacao(de:ServicoTransacao,para:ServicoTransacao):
        transacoes = de.ler()
        para.escrever(transacoes)

    @staticmethod
    def criarTabelasDB():
        
        cliente_remoto = ServicoClienteRemoto(ServiceODBC.openConnection())
        cliente_remoto.createTable()

        transacao_remoto = ServicoTransacaoRemoto(ServiceODBC.openConnection())
        transacao_remoto.createTable()

    @staticmethod
    def dropAllTables():
        ServiceODBC.deleteAllTables()

    @staticmethod
    def sumarizarDB():
        tabelas = ['CLIENTES', 'TRANSACOES']

        try:
            for item in tabelas:
                conn = ServiceODBC.openConnection()
                if ServiceODBC.checkIfTableExists(item):
                    comando_sql = f"SELECT count(id) as QTD FROM [dbo].[{item}]"
                    r =conn.cursor().execute(comando_sql)
                    row = r.fetchone()
                    print(f'Na tabela {item} temos {row[0]} registros')
                        
                        
                    conn.close()
                        

                else:
                    print(f"Tabela {item} não existe no banco de dados")

        except Error as e:
            print(f"Erro ao sumarizar dados do banco de dados : {str(e)}")
        except OSError as err:
            print("Erro de Sistema Operacional: {0}".format(err))
        except ValueError:
            print("Não foi possível fazer a conversão de tipo")
        except BaseException as err:
            print(f"Erro inesperado {err=}, {type(err)=}")
