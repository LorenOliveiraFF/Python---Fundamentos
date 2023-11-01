#Crie um programa que leia nome, sexo e idade de várias pessoas,
# guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista.
# No final, mostre:
# A) Quantas pessoas foram cadastradas
# B) A média de idade
# C) Uma lista com as mulheres
# D) Uma lista de pessoas com idade acima da média

from time import sleep
dados = {}
lista = []
opc = 'S'
while opc in 'Ss':
    dados['nome'] = input('Nome: ')
    sexo = input('Sexo: [M/ F] ')
    while True:
        if sexo in 'MmFf':
            dados['sexo'] = sexo
            break
        else:
            print('Erro! Por favor, digite apenas M ou F.')
            sexo = input('Sexo [M/ F] ')
    dados['idade'] = int(input('Idade: '))
    opc = input('Quer continuar? [S/ N] ')
    while opc not in 'SsNn':
        print('Erro! Responda apenas S ou N.')
        opc = input('Quer continuar? [S/ N] ')
    lista.append(dados.copy())
print('=*' * 30)
print(f'A) Ao todo temos {len(lista)} pessoas cadastradas!')
somaidade = 0
for i in range(0, len(lista)):
    somaidade += (lista[i]['idade'])
mediaidade = somaidade / len(lista)

print(f'B) A média de idade é de {mediaidade:.2f} anos!')
print(f'C) As mulheres cadastradas foram: ', end='')
for m in range(0, len(lista)):
    if lista[m]['sexo'] in 'Ff':
        print(f'{lista[m]["nome"]}', end=' ')
print()
print(f'D) Lista das pessoas que estão acima da média: ')
for med in range(0, len(lista)):
    if lista[med]['idade'] > mediaidade:
        print(f'{"Nome":>8} = {lista[med]["nome"]}; Sexo = {lista[med]["sexo"]}; Idade = {lista[med]["idade"]};')
print('=*' * 30)
print('ENCERRANDO...')
sleep(1)
