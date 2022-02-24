import pandas as pd
import os
from os.path import exists


class ServicePandas:

    path = os.path.abspath("files")
    header = None

    @staticmethod
    def lerPandas(i, tipo, df):
        try: 
            i+=1
            caminho = f"{tipo}{i:03d}.csv"
            if exists(caminho) and df is None:
                return ServicePandas.lerPandas(i,tipo, pd.read_csv(caminho, header=0,
                                    keep_default_na=False, sep=';'))
            elif exists(caminho):
                col_name = df.columns
                return ServicePandas.lerPandas(i,tipo, pd.concat([pd.read_csv(caminho, header=None,
                                    keep_default_na=False, sep=";", names=col_name), df]))
            else:
                return df
        except OSError as err:
            print("Erro de Sistema Operacional: {0}".format(err))
        except ValueError:
            print("Não foi possível fazer a conversão de tipo")
        except BaseException as err:
            print(f"Erro inesperado {err=}, {type(err)=}")
            
    @staticmethod
    def readDataTransacao():
        caminho = f"{ServicePandas.path}\\transaction-in-"
        transacoes_in = ServicePandas.lerPandas(0,caminho, None)

        caminho = f"{ServicePandas.path}\\transaction-out-"
        transacoes_out = ServicePandas.lerPandas(0,caminho, None)

        df_transacao = pd.concat([transacoes_in, transacoes_out])
        df_transacao.reset_index()
        df_transacao.to_csv(f"{ServicePandas.path}\\compilado_transacoes.csv",index=False, sep=";")

        print("Arquivo compilado de transações criado com sucesso")

        return f"{ServicePandas.path}\\compilado_transacoes.csv"
    @staticmethod
    def readDataCliente():
        caminho = f"{ServicePandas.path}\\clients-"
        df_cliente = ServicePandas.lerPandas(0, caminho,None)
        type(df_cliente)
        print(df_cliente)
        df_cliente.reset_index()
        df_cliente.to_csv(f"{ServicePandas.path}\\compilado_clientes.csv",index=False, sep=";")

        print("Arquivo compilado de clientes criado com sucesso")

        return f"{ServicePandas.path}\\compilado_clientes.csv"
