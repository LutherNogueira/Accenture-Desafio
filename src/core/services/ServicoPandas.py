import pandas as pd
import os
from os.path import exists


class ServicePandas:

    path = os.path.abspath("..\..\src\\db")
    @staticmethod
    def readDataTransacao():
        try: 
            for i in range(1, 10):
                caminho = f"{ServicePandas.path}\\transaction-in-{i:03d}.csv"

                if i == 1:
                    temp = pd.read_csv(caminho, header=0,
                                        keep_default_na=False, sep=";")
                    df_transacao = temp

                else:
                    col_name = df_transacao.columns
                    temp = pd.read_csv(caminho, header=None,
                                        keep_default_na=False, sep=";", names=col_name)
                    df_transacao = pd.concat([temp, df_transacao])


            for i in range(1, 64):
                caminho = f"{ServicePandas.path}\\transaction-out-{i:03d}.csv"
                col_name = df_transacao.columns
                if i == 1:
                    temp = pd.read_csv(caminho, header=None, skiprows=1, keep_default_na=False, sep=";", names=col_name)
                    df_transacao = pd.concat([temp, df_transacao])
                else:
                    col_name = df_transacao.columns
                    temp = pd.read_csv(caminho, header=None,
                                    keep_default_na=False, sep=";", names=col_name)
                    df_transacao = pd.concat([temp, df_transacao])
            df_transacao.reset_index()
            df_transacao.to_csv(f"{ServicePandas.path}\\compilado_transacoes.csv",index=False, sep=";")

            print("Arquivo compilado de transações criado com sucesso")

            return f"{ServicePandas.path}\\compilado_transacoes.csv"
        except OSError as err:
            print("Erro de Sistema Operacional: {0}".format(err))
        except ValueError:
            print("Não foi possível fazer a conversão de tipo")
        except BaseException as err:
            print(f"Erro inesperado {err=}, {type(err)=}")

    def readDataCliente():
        try:
            for i in range(1, 5):
                caminho = f"{ServicePandas.path}\\clients-{i:03d}.csv"
                if i == 1:
                    temp = pd.read_csv(caminho, header=0,
                                    keep_default_na=False, sep=";")
                    df_cliente = temp

                else:
                    col_name = df_cliente.columns
                    temp = pd.read_csv(caminho, header=None,
                                    keep_default_na=False, sep=";", names=col_name)
                    df_cliente = pd.concat([temp, df_cliente])

            df_cliente.reset_index()
            df_cliente.to_csv(f"{ServicePandas.path}\\compilado_clientes.csv",index=False, sep=";")
            print("Arquivo compilado de clientes criado com sucesso")

            return f"{ServicePandas.path}\\compilado_clientes.csv"

        except OSError as err:
            print("Erro de Sistema Operacional: {0}".format(err))
        except ValueError:
            print("Não foi possível fazer a conversão de tipo")
        except BaseException as err:
            print(f"Erro inesperado {err=}, {type(err)=}")
