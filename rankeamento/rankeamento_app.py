import pandas as pd
from pandas import read_csv

df_notas = read_csv('../coleta_notas/lista_notas.csv')
df_nomes = read_csv('../coleta_nomes/lista_nomes.csv')

print(df_notas)
print(df_nomes)