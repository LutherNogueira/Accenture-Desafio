import pandas as pd
import os

path = os.path.abspath(".")

for i in range(1,10):
  caminho=f"{path}\\transaction-in-{i:03d}.csv"
  
  if i == 1:
    temp = pd.read_csv(caminho, header=0, keep_default_na=False, sep=";")
    df = temp

  else:
    col_name = df.columns
    temp = pd.read_csv(caminho, header=None, keep_default_na=False, sep=";", names=col_name)
    df =  pd.concat([temp,df])

    

for i in range(1,64):
  caminho=f"{path}\\transaction-out-{i:03d}.csv"
  if i == 1:
    temp = pd.read_csv(caminho, header=0, keep_default_na=False, sep=";")
    df = temp

  else:
    col_name = df.columns
    temp = pd.read_csv(caminho, header=None, keep_default_na=False, sep=";", names=col_name)
    df =  pd.concat([temp,df])

  for i in range(1,5):
    caminho=f"{path}\\clients-{i:03d}.csv"
    if i == 1:
      temp = pd.read_csv(caminho, header=0, keep_default_na=False, sep=";")
      df2 = temp

    else:
      col_name = df2.columns
      temp = pd.read_csv(caminho, header=None, keep_default_na=False, sep=";", names=col_name)
      df2 =  pd.concat([temp,df2])

df.to_csv('resultado.csv', index=False)
df2.to_csv('resultado_cliente.csv', index=False)

df2.reset_index()

print(len(df))
print(df)

