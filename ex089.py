# Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.
# No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas
# de cada aluno individualmente.

from time import sleep
lista = []
boletim = []
opc = 'S'
while opc in 'Ss':
    nome = input('Nome: ')
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2)/ 2
    lista.append(nome)
    lista.append(nota1)
    lista.append(nota2)
    lista.append(media)
    boletim.append(lista[:])
    lista.clear()
    opc = input('Quer continuar? [S/N]: ')
    while opc not in 'SsNn':
        opc = input('Opção inválida! Quer continuar? [S/N]: ')
print('=' * 35)
print(f'{"No.":<2} {"Nome":<10} {"Média":>10} ')
print('-' * 35)
for pos, aluno in enumerate(boletim):
    print(f' {pos:<2} {aluno[0]:<10} {aluno[3]:>10}')
escolUsuario = int(input('Mostrar notas de qual aluno? (999 PARA INTERROMPER): '))
while escolUsuario != 999:
    print(f'Notas de {boletim[escolUsuario][0]} são [{boletim[escolUsuario][1], boletim[escolUsuario][2]}]')
    escolUsuario = int(input('Mostrar notas de qual aluno? (999 PARA INTERROMPER): '))
print('Finalizando...')
sleep(2)
print(' <<< VOLTE SEMPRE >>>')
