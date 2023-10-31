#Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.

num = int(input('Digite um número:'))
numpar = num % 2
if numpar == 0:
    print('O número é PAR!')
else:
    print('O número é ÍMPAR!')
print(type(numpar))
