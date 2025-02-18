import pandas as pd
from pandas import read_csv

df_notas = read_csv('../coleta_notas/lista_notas.csv')
df_nomes = read_csv('../coleta_nomes/lista_nomes.csv')

df_merged = pd.merge(df_notas, df_nomes, on='insc', how='inner')

#df_merged[['nota1', 'nota2', 'nota3', 'nota4', 'red']]

pesos = [1, 1, 2, 2, 2]
pl = 1
ph = 1
pn = 2
pm = 2
pred = 2
valores = []
medias = []

def valores():
    global medias
    for item in df_merged.values:
        c = soma = media = 0
        nota_lin = nota_hum = nota_nat = nota_mat = nota_red = 0
        for nota in item[1:6]:
            if c == 0:
                nota_lin = nota*pl
            elif c == 1:
                nota_hum = nota*ph
            elif c == 2:
                nota_nat = nota*pn
            elif c == 3:
                nota_mat = nota*pm
            elif c == 4:
                nota_red = nota*pred
            soma += nota
            c += 1
        soma_pesos = nota_lin + nota_hum + nota_nat + nota_mat + nota_red
        media = soma_pesos / soma
        nome = item[6]
        medias.append([media,nome])
print(medias)
medias.sort()
for media in medias:
    print(media)
valores()
