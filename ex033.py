#Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
num1 = int(input('Digite o primeiro número:'))
num2 = int(input('Digite o segundo número:'))
num3 = int(input('Digite o terceiro número:'))
lista = [num1, num2, num3]
maxLista = max(lista)
minLista = min(lista)
print('O maior número é {}'.format(maxLista))
print('O menor número é {}'.format(minLista))


