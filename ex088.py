#Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
# O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.

from random import randint
from time import sleep

print('-' * 15)
print('JOGO DA MEGA SENA')
print('-' * 35)
mega = []
sorteados = 0
jogos = int(input('Quantos jogos serão gerados? '))
print(f'Sorteando {jogos} jogos!')
for c in range(1, jogos+1):
    sleep(1)
    print(f'Jogo {c}: ', end='')
    for numeros in range(1, 7):
        sorteados = randint(1, 60)
        if sorteados not in mega:
            mega.append(sorteados)
        elif sorteados in mega:
            sorteados = randint(1, 60)
            if sorteados not in mega:
                mega.append(sorteados)
        if numeros >= 6:
            print(mega, end='')
            mega.clear()
    print()
print('-' * 35)
print('BOA SORTE!')
