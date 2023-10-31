#Crie um programa que leia um número real qualquer e mostre na tela sua
#Porção inteira - Ex: 6.127. O número 6.127 tem a parte inteira 6.

from math import trunc
numero = float(input('Digite um número real:'))
parteInteira = trunc(numero)
print('O número {} tem a parte inteira de {}.'.format(numero, parteInteira))
