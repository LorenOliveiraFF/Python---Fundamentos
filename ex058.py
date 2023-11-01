# Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10.
# Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

from random import randint
from time import sleep

tentativas = 1
print('===== DESAFIO =====')
print('Vou pensar em um número de 0 a 10, tente adivinhar!')
numeroComp = randint(0, 10)
numeroJog = int(input('Qual sua escolha? '))
print('Processando...')
sleep(2)
while numeroJog != numeroComp:
    numeroJog = int(input('Você errou! Tente novamente! Qual sua escolha? '))
    tentativas += 1
print('Você acertou, o número do computador foi {}. Você precisou de um total de {} tentativa(s)!'.format(numeroComp, tentativas))
