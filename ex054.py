# Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas
# ainda não atingiram a maioridade e quantas já são maiores.

from datetime import datetime
contadorMaioridade = 0
contadorMenores = 0
anoatual = datetime.now().year
for pessoa in range(1, 8):
    ano = int(input('Em que ano a {}º pessoa nasceu?'.format(pessoa)))
    if (anoatual - ano) >= 18:
        contadorMaioridade += 1
    else:
        contadorMenores += 1
print('Ao todo tivemos {} pessoas maiores de idade!'.format(contadorMaioridade))
print('E também tivemos {} pessoas menores de idade!'.format(contadorMenores))
