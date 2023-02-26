from modulo_danificado import*
from math import exp
n1=int(input('Digite um número'))
n2=int(input('Digite outro'))
op=int(input('1-SOMA 2- SUB  3-DIV 4-MULT 5-EXPO 0-SAIR'))
if op==1:
    danificado_na_soma(n1,n2)
if op==2:
    danificado_na_sub(n1,n2)
if op==3:
    danificado_na_div(n1,n2)
if op==4:
    danificado_na_mult(n1,n2)
if op==5:
    exp(n1)
if op==6:
    saida()


