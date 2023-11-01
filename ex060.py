#Faça um programa que leia um número qualquer e mostre o seu fatorial.
print('=' * 12, 'FATORIAL', '=' * 12)
escolha = int(input('Qual o número escolhido? '))
numfat = escolha
contador = escolha
print('Calculando {}! = {}'.format(numfat, numfat), end=' ')
while contador > 1:
    contador -= 1
    fatorial = escolha * contador
    escolha = fatorial
    print('x', contador, end=' ')
print('=', escolha, end='')
