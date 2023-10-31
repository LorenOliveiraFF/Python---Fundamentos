#Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.
metros = float(input('Insira o valor em Metros:'))
centimetros = metros * 100
milimetros = metros * 1000
print('O valor digitado em METROS: {}, em CENTÍMETROS: {}, e em MILÍMETROS: {}.'.format(metros, centimetros, milimetros))
