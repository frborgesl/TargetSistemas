from pandas import read_json
from numpy import where

df = read_json("dados.json")
menor = df["valor"].min()

lista = list(where(df["valor"] == menor)[0])
print(df.iloc[lista])