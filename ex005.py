#Faça um programa que leia um número inteiro e mostre na tela seu sucessor e antecessor.
numero = int(input('Digite um número:'))
sucessor = numero + 1
antecessor = numero - 1
print('Seu número foi: {}! O sucessor dele é {}, e o antecessor é {}.'.format(numero, sucessor, antecessor))
