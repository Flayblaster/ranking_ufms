from pypdf import PdfReader
import pandas as pd

paginas = []
c = 0

lista_concorrentes = pd.read_csv('../coleta/lista_tratada.csv')
reader = PdfReader("edital_notas.pdf")
number_of_pages = len(reader.pages)
print(lista_concorrentes['col_insc'])

def inicio():
    for pages in range(4, number_of_pages):
        page = reader.pages[pages]
        remov_inutil(page)
    print(paginas)

def remov_inutil(page):
    text = page.extract_text()
    text = text.replace(text[0:229], '')
    text = text.replace(text[-59:], '')
    text = text.replace(',', '.')
    text = text.replace(' ', '/')
    alunos = text.split()
    return filtro(alunos)

def filtro(alunos):
    lista_de_insc = lista_concorrentes['col_insc']
    resul = lista_de_insc.isin([1128143])
    print(resul)
inicio()