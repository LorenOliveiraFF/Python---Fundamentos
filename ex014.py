#Faça um programa que receba um valor em Cº e calcule o valor correspondente em Fahrenheit.
celsius = float(input('Digite a temperatura em Cº:'))
fahrenheit = 9 * celsius / 5 + 32
print('A temperatura {}ºC corresponde a {:.1f}ºF!'.format(celsius, fahrenheit))
