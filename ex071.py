# Crie um programa que simule o funcionamento de um caixa eletrônico.
# No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.
# OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.

from time import sleep

print('=' * 40)
print('{:^40}'.format('BANCO LOREN E FERNANDO'))
print('=' * 40)
valor = int(input('Qual valor você quer sacar? R$ '))

cedulas50 = 0
cedulas20 = 0
cedulas10 = 0
cedulas1 = 0

while True:
    cedulas50 = valor // 50
    valor = valor - (cedulas50 * 50)
    if valor >= 20:
        cedulas20 = valor // 20
        valor = valor - (cedulas20 * 20)
    if valor >= 10:
        cedulas10 = valor // 10
        valor = valor - (cedulas10 * 10)
    if valor >= 1:
        cedulas1 = valor // 1
        valor = valor - (cedulas1 * 1)
    break

print('Foram utilizadas:')
print(f'{cedulas50} notas de R$50.00!')
print(f'{cedulas20} notas de R$20.00!')
print(f'{cedulas10} notas de R$10.00!')
print(f'{cedulas1} notas de R$1.00!')
sleep(1)
print('Volte sempre ao Banco L & F!')






