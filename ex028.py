# Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça para o usuário tentar
# descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import randint
from time import sleep

print('-=-' * 20)
print('Vou pensar em um número de 0 a 5, tente adivinhar!')
print('-=-' * 20)
numero = randint(0, 5)
numusuario = int(input('Em que número eu pensei?'))
print('Processando...')
sleep(3)
if numero == numusuario:
    print('PARABÉNS! Você me venceu!')
else:
    print('GANHEI! Pensei no número {}, e não no {}!'.format(numero, numusuario))
