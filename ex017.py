#Faça um programa que leia o comprimento do cateto oposto e
#Do cateto adjacente, calcule e mostre o comprimento da hipotenusa

from math import hypot
catOposto = float(input('Comprimento do Cateto Oposto:'))
catAdjacente = float(input('Comprimento do Cateto Adjacente:'))
hipotenusa = hypot(catOposto, catAdjacente)
print('A hipotenusa é {:.2f}'.format(hipotenusa))