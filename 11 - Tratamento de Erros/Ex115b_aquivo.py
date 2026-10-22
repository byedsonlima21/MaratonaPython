from Ex115_Menu import *

def arquivoExiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False

def criarArquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print("Houve um erro na criação do arquivo")

def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print("Houve um erro")
    else:
        cabecalho('PESSOAS CADASTRADAS')
        print(a.read())
