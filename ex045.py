#Crie um programa que faça o computador jogar Jokenpô com você.
from random import randint
from time import sleep

print('Suas opções:'    
      '\n [1] PEDRA'
      '\n [2] PAPEL'
      '\n [3] TESOURA')
opcaoJog = int(input('Qual a sua escolha?'))
pedra = 1
papel = 2
tesoura = 3

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
sleep(1)
print('=' * 15)

escolhaComp = randint(1, 3)
if (opcaoJog == pedra) and (escolhaComp == pedra) or (opcaoJog == papel) and (escolhaComp == papel) or (opcaoJog == tesoura) and (escolhaComp == tesoura):
    if opcaoJog == pedra:
        print('Jogador: PEDRA! \nComputador: PEDRA!')
        print('=' * 15)
        print('EMPATE')
    elif opcaoJog == papel:
        print('Jogador: PAPEL! \nComputador: PAPEL!')
        print('=' * 15)
        print('EMPATE')
    elif opcaoJog == tesoura:
        print('Jogador: TESOURA! \nComputador: TESOURA!')
        print('=' * 15)
        print('EMPATE')
elif opcaoJog == pedra:
    if escolhaComp == papel:
        print('Jogador: PEDRA! \nComputador: PAPEL!')
        print('=' * 15)
        print('Computador venceu!')
    elif escolhaComp == tesoura:
        print('Jogador: PEDRA! \nComputador: TESOURA!')
        print('=' * 15)
        print('Jogador venceu!')
elif opcaoJog == papel:
    if escolhaComp == pedra:
        print('Jogador: PAPEL! \nComputador: PEDRA!')
        print('=' * 15)
        print('Jogador venceu!')
    elif escolhaComp == tesoura:
        print('Jogador: PAPEL! \nComputador: TESOURA!')
        print('=' * 15)
        print('Computador venceu!')
elif opcaoJog == tesoura:
    if escolhaComp == pedra:
        print('Jogador: TESOURA! \nComputador: PEDRA!')
        print('=' * 15)
        print('Computador venceu!')
    elif escolhaComp == papel:
        print('Jogador: TESOURA! \nComputador: PAPEL!')
        print('=' * 15)
        print('Jogador venceu!')
else:
    print('Opção inválida!')
