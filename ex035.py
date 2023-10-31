# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

num1 = float(input('Digite o primeiro número: '))
num2 = float(input('Digite o primeiro número: '))
num3 = float(input('Digite o primeiro número: '))

cond1 = num1 < num2 + num3
cond2 = num2 < num1 + num3
cond3 = num3 < num1 + num2

if cond1 and cond2 and cond3:
    print('É possível formar um triângulo!')
else:
    print('Não é possível formar um triângulo!')
