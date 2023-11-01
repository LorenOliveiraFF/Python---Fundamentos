#Desenvolva um programa que leia 4 valores pelo teclado e guarde-os em uma tupla. No final, mostre:
# a) Quantas vezes apareceu o número 9.
# b) Em que posição foi digitado o primeiro valor 3.
# c) Quais foram os números pares.

descobretres = 0

num1 = int(input('Numero 1:'))
num2 = int(input('Numero 2:'))
num3 = int(input('Numero 3:'))
num4 = int(input('Numero 4:'))
tupla = (num1, num2, num3, num4)

print(f'Você digitou os valores {tupla}')

contanove = tupla.count(9)
print(f'O número 9 apareceu {contanove} vez(es)!')

conttres = tupla.count(3)
if conttres == 0:
    print('O valor 3 não foi digitado em nenhuma posição!')
else:
    descobretres = tupla.index(3)
    print(f'O valor 3 apareceu na {descobretres + 1}ª posição!')

print('Os valores pares digitados foram: ', end='')
for c in tupla:
    if c % 2 == 0:
        print(c, end='')
