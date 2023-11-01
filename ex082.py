#Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente.
# Ao final, mostre o conteúdo das três listas geradas.

lista = []
opc = 'S'
while opc in 'Ss':
    num = int(input('Digite um valor: '))
    lista.append(num)
    opc = str(input('Quer continuar [S/N]: '))
    while opc not in 'SsNn':
        opc = str(input('Inválido! Quer continuar [S/N]: '))

pares = []
impares = []
for v in lista:
    if v % 2 == 0:
        pares.append(v)
    else:
        impares.append(v)
print('A lista completa é:', lista)
print('Pares:', pares)
print('Impares:', impares)
