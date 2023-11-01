# Crie um programa que vai gerar 5 números aleatórios e colocá-los em uma Tupla.
# Depois, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.

from random import randint

numeros = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1,10), randint(1, 10))
maximo = max(numeros)
menor = min(numeros)
print(f'Os valores sorteados foram: {numeros}')
print(f'O maior valor sorteado foi: {maximo}')
print(f'O menor valor sorteado foi: {menor}')

#Outro Jeito
print('O maior valor foi:', sorted(numeros)[-1])
print('O menor valor foi:', sorted(numeros)[0])
