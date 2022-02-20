import pandas as pd
import os
from os.path import exists

path = os.path.abspath("src\\db")

def readDataTransationIn(i,count):

  dir=f"{path}\\transaction-in-{i:03d}.csv"

  while True:
    count+=1
    if i == 1:
      temp = pd.read_csv(dir, header=0, keep_default_na=False, sep=";")
      df = temp
    else:
      col_name = df.columns
      temp = pd.read_csv(dir, header=None, keep_default_na=False, sep=";", names=col_name)
      df =  pd.concat([temp,df])
    if exists(dir):
      readDataTransationIn(i+1,count)

def readDataTransationOut(i,count):

  dir=f"{path}\\transaction-out-{i:03d}.csv"

  while True:
    count+=1
    if i == 1:
      temp = pd.read_csv(dir, header=0, keep_default_na=False, sep=";")
      df = temp
    else:
      col_name = df.columns
      temp = pd.read_csv(dir, header=None, keep_default_na=False, sep=";", names=col_name)
      df =  pd.concat([temp,df])
    if exists(dir):
      readDataTransationOut(i+1,count)

def readDataClient(i,count):

  dir=f"{path}\\clients-{i:03d}.csv"

  while True:
    count+=1
    if i == 1:
      temp = pd.read_csv(dir, header=0, keep_default_na=False, sep=";")
      df = temp
    else:
      col_name = df.columns
      temp = pd.read_csv(dir, header=None, keep_default_na=False, sep=";", names=col_name)
      df2 =  pd.concat([temp,df2])
    if exists(dir):
      readDataClient(i+1,count)


df.to_csv('resultado.csv', index=False)

df2.to_csv('resultado_cliente.csv', index=False)

df2.reset_index()

print(len(df))
print(df)