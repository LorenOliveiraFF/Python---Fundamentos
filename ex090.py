# Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário.
# No final, mostre o conteúdo da estrutura na tela.

print('=' * 30)
notas = dict()
notas['nome'] = input('Nome: ')
notas['média'] = float(input('Média: '))
print('=' * 30)
print(f' - Nome é igual a {notas["nome"]}!')
print(f' - Média é igual a {notas["média"]}')

situ = ''
if notas['média'] <= 5:
    situ = 'Reprovado!'
elif 5 < notas['média'] <= 6.5:
    situ = 'Recuperação!'
else:
    situ = 'Aprovado!'
print(f' - Situação é igual a: {situ}')
