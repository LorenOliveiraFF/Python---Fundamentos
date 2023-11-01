# Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar().
# A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função
# vai mostrar a soma entre todos os valores pares sorteados pela função anterior.
from random import randint
from time import sleep


def sorteia():
    numeros = []
    print(f'Sorteando os valores da LISTA: [ ', end='')
    sleep(1)
    for c in range(1, 6):
        sleep(0.8)
        num = randint(1, 10)
        print(num, end=' ')
        numeros.append(num)
    sleep(0.2)
    print('] PRONTO!')
    somapar(numeros)


def somapar(lst):
    soma = 0
    print(f'Somando os valores PARES de {lst}, temos: ', end='')
    for c in lst:
        if c % 2 == 0:
            soma += c
    print(f'{soma}!')


sorteia()
