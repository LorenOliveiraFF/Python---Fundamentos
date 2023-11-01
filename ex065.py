# Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os
# valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer
# ou não continuar a digitar valores.

from statistics import mean
opc = 'S'
lista = []
cont = media = maximo = minimo = 0

while opc == 'S':
    num = int(input('Digite um número: '))
    lista.append(num)
    opc = str(input('Quer continuar? [S/N]: '))
    cont += 1
    media = mean(lista)
    maximo = max(lista)
    minimo = min(lista)
print('Você digitou {} números e a média foi {}'.format(cont, media))
print('O maior valor foi {} e o menor foi {}'.format(maximo, minimo))

#OU

opc = 'S'
cont = soma = media = 0
maior = menor = 0

while opc == 'S':
    num = int(input('Digite um número: '))
    soma += num
    cont += 1
    if cont == 1:
        menor = num
        maior = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    opc = str(input('Quer continuar? [S/N]: '))
media = soma / cont

print('Você digitou {} números e a média foi {:.2f}!'.format(cont, media))
print('O maior valor foi {} e o menor foi {}!'.format(maior, menor))


