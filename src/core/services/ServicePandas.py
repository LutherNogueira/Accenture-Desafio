import pandas as pd
import os
from os.path import exists


class ServicePandas:

    path = os.path.abspath("src\\db")
    @staticmethod
    def readDataTransation():
        for i in range(1, 10):
            caminho = f"{path}\\arquivos_carga_csv\\transaction-in-{i:03d}.csv"

            if i == 1:
                temp = pd.read_csv(caminho, header=0,
                                    keep_default_na=False, sep=";")
                df_transacao = temp

            else:
                col_name = df.columns
                temp = pd.read_csv(caminho, header=None,
                                    keep_default_na=False, sep=";", names=col_name)
                df_transacao = pd.concat([temp, df_transacao])


        for i in range(1, 64):
            caminho = f"{path}\\arquivos_carga_csv\\transaction-out-{i:03d}.csv"
            col_name = df_transacao.columns
            if i == 1:
                temp = pd.read_csv(caminho, header=None, skiprows=1, keep_default_na=False, sep=";", names=col_name)

            else:
                col_name = df_transacao.columns
                temp = pd.read_csv(caminho, header=None,
                                keep_default_na=False, sep=";", names=col_name)
                df_transacao = pd.concat([temp, df_transacao])
        df_transacao.reset_index()
        return df_transacao

    def readDataCliente():
        for i in range(1, 5):
            caminho = f"{path}\\arquivos_carga_csv\\clients-{i:03d}.csv"
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
        return df_cliente.to_csv(index=False)


'''
  @staticmethod
  def readDataTransationIn(i, count):

      dir = f"{path}\\transaction-in-{i:03d}.csv"

      while True:
          count += 1
          if i == 1:
              temp = pd.read_csv(dir, header=0, keep_default_na=False, sep=";")
              df = temp
          else:
              col_name = df.columns
              temp = pd.read_csv(
                  dir, header=None, keep_default_na=False, sep=";", names=col_name)
              df = pd.concat([temp, df])

          if exists(dir):
              readDataTransationIn(i+1, count)

  @staticmethod
  def readDataTransationOut(i, count):

      dir = f"{path}\\transaction-out-{i:03d}.csv"

      while True:
          count += 1
          if i == 1:
              temp = pd.read_csv(dir, header=0, keep_default_na=False, sep=";")
              df = temp
          else:
              col_name = df.columns
              temp = pd.read_csv(
                  dir, header=None, keep_default_na=False, sep=";", names=col_name)
              df = pd.concat([temp, df])
          if exists(dir):
              readDataTransationOut(i+1, count)

  @staticmethod
  def readDataClient(i, count):

      dir = f"{path}\\clients-{i:03d}.csv"

      while True:
          count += 1
          if i == 1:
              temp = pd.read_csv(dir, header=0, keep_default_na=False, sep=";")
              df = temp
          else:
              col_name = df.columns
              temp = pd.read_csv(
                  dir, header=None, keep_default_na=False, sep=";", names=col_name)
              df2 = pd.concat([temp, df2])
          if exists(dir):
              readDataClient(i+1, count)

'''
    
