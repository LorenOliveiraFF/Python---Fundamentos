#Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# – EQUILÁTERO: todos os lados iguais
# – ISÓSCELES: dois lados iguais, um diferente
# – ESCALENO: todos os lados diferentes

num1 = float(input('Digite o primeiro número: '))
num2 = float(input('Digite o primeiro número: '))
num3 = float(input('Digite o primeiro número: '))

cond1 = num1 < num2 + num3
cond2 = num2 < num1 + num3
cond3 = num3 < num1 + num2

if cond1 and cond2 and cond3:
    if num1 == num2 and num1 == num3:
        print('É possível formar um triângulo EQUILÁTERO!')
    elif num1 != num2 and num1 != num3:
        print('É possível formar um triângulo ESCALENO!')
    else:
        print('É possível formar um triângulo ISÓSCELES!')
else:
    print('Não é possível formar um triângulo!')
