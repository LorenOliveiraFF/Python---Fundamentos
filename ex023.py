#Faça um programa que leia um número de 0 a 9999 e mostre na tela
#Cada um dos dígitos separados

num = int(input('Digite um número entre 0 e 9999:'))
print('Unidade:', num // 1 % 10)
print('Dezena:', num // 10 % 10)
print('Centena:', num // 100 % 10)
print('Milhar:', num // 1000 % 10)
