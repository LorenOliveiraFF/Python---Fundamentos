#Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

numero = int(input('Digite um número:'))
contador = 0
for c in range(1, numero+1):
    if numero % c == 0:
        cor = {'limpa': '\033[m', 'amarelo': '\033[33m'}
        print('{}{}{}'.format(cor['amarelo'], c, cor['limpa']), end=' ')
        contador += 1
    else:
        cor = {'limpa': '\033[m', 'vermelho': '\033[31m'}
        print('{}{}{}'.format(cor['vermelho'], c, cor['limpa']), end=' ')
print('\nO número {} foi dividido por {} vezes!'.format(numero, contador))
if contador <= 2:
    print('E é um número primo!')
else:
    print('E por este motivo, não é primo!')
