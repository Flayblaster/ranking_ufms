from pypdf import PdfReader
import pandas as pd

reader = PdfReader("edital_notas.pdf")
number_of_pages = len(reader.pages)


def extracao():
    """
    extrai todo o conteúdo das páginas.
    :return: retorna o conteúdo das páginas, limpo e tratado.
    """
    global pages
    lista = []
    for pages in range(4, 359):
        page = reader.pages[pages]
        conteudo = page.extract_text()
        conteudo = conteudo.split('\n')
        conteudo_limpo = limpeza(conteudo)
        lista.extend(conteudo_limpo)
    gerador_df(lista)

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
    df = pd.DataFrame(conteudo, columns=['insc', 'nota1', 'nota2', 'nota3', 'nota4', 'red'])
    df.to_csv('lista_notas.csv', index=False)


extracao()