# Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: o nome de um jogador
# e quantos gols ele marcou.
# O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.


def ficha(nome='', gols=''):
    if gols.isnumeric():
        if nome == '':
            print(f'O jogador <desconhecido> fez {gols} gol(s) no campeonato!')
        else:
            print(f'O jogador {nome} fez {gols} gol(s) no campeonato!')
    else:
        if nome == '' and gols == '':
            print(f'O jogador <desconhecido> fez 0 gol(s) no campeonato!')
        else:
            print(f'O jogador {nome} fez 0 gol(s) no campeonato!')


nomear = str(input('Nome: '))
golmarcado = str(input('Gols Marcados: '))
ficha(nomear, golmarcado)

