from operator import index

from pypdf import PdfReader
import pandas as pd

paginas = []
c = 0

lista_concorrentes = pd.read_csv('../coleta/lista_tratada.csv')
reader = PdfReader("edital_notas.pdf")
number_of_pages = len(reader.pages)
print(lista_concorrentes['col_insc'])

def inicio():
    for pages in range(4, 6):
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
    lista_de_insc = list(lista_concorrentes['col_insc'])
    for aluno in alunos:
        aluno = aluno.split('/')
        if aluno[0] in lista_de_insc:
            print('cu')
inicio()