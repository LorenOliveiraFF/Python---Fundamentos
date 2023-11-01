# Faça um programa que jogue par ou impar com o computador.
# O jogo só será encerrado quando o jogador PERDER, mostrando o total de vitórias consecutivas
# que ele conquistou no final do jogo

from random import randint

soma = 0
contadorVit = 0
print('-=-' * 8)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('-=-' * 8)
while True:
    valor = int(input('Digite um valor: '))
    computador = randint(0, 10)
    soma = valor + computador
    resto = soma % 2
    parimpar = input('Par ou Ímpar? [P/ I] ').strip().upper()
    print(f'Você jogou {valor} e o computador {computador}. Total deu {soma}. ', end='')
    print('Deu PAR!' if resto == 0 else 'Deu ÍMPAR!')
    if parimpar == 'P' and resto == 0:
        print('Você GANHOU!')
        contadorVit += 1
    elif parimpar == 'I' and resto == 1:
        print('Você GANHOU!')
        contadorVit += 1
    else:
        print('Você PERDEU!')
        break
print('-=-' * 8)
print(f'GAME OVER! Você venceu {contadorVit} vez(es)!')
