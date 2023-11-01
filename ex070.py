# Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
# A) qual é o total gasto na compra.
# B) quantos produtos custam mais de R$1000.
# C) qual é o nome do produto mais barato.

print('*' * 40)
print('          LOJA SUPER BARATÃO        ')
print('*' * 40)

continua = 's'
somaprod = 0
maisdemil = 1000
contprod = 0
menornome = ''
maior = menor = quant = 0


while True:
    nomeprod = input('Nome do produto: ')
    precoprod = float(input('Preço: R$'))
    continua = input('Quer continuar? [S/ N] ').strip().lower()
    quant += 1
    if quant == 1:
        maior = menor = precoprod
    else:
        if precoprod > maior:
            maior = precoprod
        if precoprod < menor:
            menor = precoprod
            menornome = nomeprod
    while continua != 's' and continua != 'n':
        continua = input('Quer continuar? [S/ N] ').strip().lower()
    somaprod += precoprod
    if precoprod > maisdemil:
        contprod += 1
    if continua in 'n':
        break
print('-' * 20, ' FIM DO PROGRAMA ', '-' * 20)
print(f'O total da compra foi de R${somaprod:.2f}.')
print(f'Temos {contprod} produto(s) custando mais de RS1000.00.')
print(f'O produto mais barato foi a/o {menornome} e custa R${menor:.2f}.')
