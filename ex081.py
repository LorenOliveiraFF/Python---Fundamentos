#Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, mostre:
# A) Quantos números foram digitados.
# B) A lista de valores, ordenada de forma decrescente.
# C) Se o valor 5 foi digitado e está ou não na lista.

lista = []
opc = 'S'
while opc in 'Ss':
    num = int(input('Digite um valor: '))
    lista.append(num)
    opc = str(input('Quer continuar? [S/N]: '))
    while opc not in 'SsNn':
        opc = str(input('Opção inválida, quer continuar? [S/N]: '))
print(f'Você digitou {len(lista)} elementos!')
print(f'Os valores em ordem decrescente são: {sorted(lista, reverse=True)}')
# lista.sort(reverse=True)
cont5 = lista.count(5)
if cont5 == 0:
    print('O valor 5 não foi digitado!')
if cont5 >= 1:
    print('O valor 5 está presente na lista!')
