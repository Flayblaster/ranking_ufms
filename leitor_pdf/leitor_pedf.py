from pypdf import PdfReader
import pandas as pd

reader = PdfReader("edital_notas.pdf")
number_of_pages = len(reader.pages)


def extracao():
    """
    extrai todo o conteúdo das páginas.
    :return: retorna o conteúdo das páginas, limpo e tratado.
    """
    for pages in range(4, 6):
        page = reader.pages[pages]
        conteudo = page.extract_text()
        conteudo = conteudo.split('\n')
    gerador_df(limpeza(conteudo))


def limpeza(conteudo_sujo):
    """
    Faz a limpeza de todo o conteudo, retornado uma lista com inscrição e notas
    :param conteudo_sujo: É o conteudo cru da página
    :return:
    """
    conteudo_limpo = []
    conteudo_sujo = conteudo_sujo[6:]
    conteudo_sujo.pop(-1)
    for item in conteudo_sujo:
        item = item.replace(',', '.')
        item = item.split()
        item.pop(1)
        conteudo_limpo.append(item)
    return conteudo_limpo

def gerador_df(conteudo):
    for x in range(2):
        if x == 0:
            print('1ndad')
        else:
            conteudo.extend(conteudo)
    for item in conteudo:
        count += 1
    #conteudo.to_csv('lista_notas.csv', index=False)


extracao()