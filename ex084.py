#Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves.

dado = []
lista = []
pesos = []
opc = 'S'
while opc in 'Ss':
    nome = str(input('Nome: '))
    peso = float(input('Peso: '))
    dado.append(nome)
    dado.append(peso)
    lista.append(dado[:])
    dado.clear()
    opc = str(input('Quer continuar? [S/N]: '))
    while opc not in 'SsNn':
        opc = str(input('Opção inválida! Quer continuar? [S/N]: '))
print(f'Foram cadastradas {len(lista)} pessoas!')
for peso in lista:
    pesos.append(peso[1])
maxpeso = max(pesos)
minpeso = min(pesos)

pessoamaior = []
pessoamenor = []
for p in lista:
    if p[1] == maxpeso:
        pessoamaior.append(p[0])
    elif p[1] == minpeso:
        pessoamenor.append(p[0])
print(f'O maior peso foi de: {max(pesos)} e foi da/ do {pessoamaior} ')
print(f'O menor peso foi de: {min(pesos)} e foi da/ do: {pessoamenor}')
