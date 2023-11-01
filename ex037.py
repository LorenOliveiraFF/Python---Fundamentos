#Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
# 1 para binário, 2 para octal e 3 para hexadecimal.
num = int(input('Digite um número inteiro:'))
base = int(input('Escolha uma das bases para conversão:'
                 '\n [1] Converter para BINÁRIO'
                 '\n [2] Converter para OCTAL'
                 '\n [3] Converter para HEXADECIMAL'
                 '\n Sua opção:'))
if base == 1:
    conver = bin(num)
    print('O número {} convertido para BINÁRIO é igual a {}.'.format(num, conver[2:]))
elif base == 2:
    conver = oct(num)
    print('O número {} convertido para OCTAL é igual a {}.'.format(num, conver[2:]))
elif base == 3:
    conver = hex(num)
    print('O número {} convertido para HEXADECIMAL é igual a {}.'.format(num, conver[2:]))
else:
    print('Parece que você digitou uma opção que não está disponível, tente novamente!')
