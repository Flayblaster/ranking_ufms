import pandas as pd

df_inicial = pd.read_csv('edital_nomes_online.csv')

df = pd.DataFrame({
    'col_insc':[],
    'col_nome':[],
})

def main(df):
    """
    Junta e organiza todas as funcoes, ela lança os dados para a adcionar ao df
    :param df:
    :return:
    """
    nome = []
    insc = []
    for item in df['pala']:
        n_curso = item[83:88]
        tipo_vaga = item[185:187]
        if selecao(n_curso, tipo_vaga):
            nome.append(trata(item[10:52]))
            insc.append(trata(item[0:7]))
    df_append(insc, nome)

def selecao(c, t_v):
    """
    retorna True se a condição for verdadeira, ela verifica se o candidato corrensponde ao curso desejado
    :param c: numero do curso
    :param t_v: tipo de vaga
    :return: True or False
    """
    if '2304' in c and 'AC' in t_v:
        return True

def df_append(i, n):
    """
    Essa função adciona os valores de i e n ao DataFrame
    :param i: É o numero de inscrição do candidato
    :param n: É o nome do candidato
    :param count: Somente um contador de indexação do loc
    :return: não retorna nada
    """
    df['col_insc'] = i
    df['col_nome'] = n

def trata(item):
    return item.strip().upper()

main(df_inicial)
df.to_csv('lista_tratada.csv', index=False)

