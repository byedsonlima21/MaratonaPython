from Ex112.utilidades import moeda
from Ex112.utilidades import dado

m = dado.leia_dinheiro('Digite um valor: R$')
moeda.resumo(m, 15, 74)