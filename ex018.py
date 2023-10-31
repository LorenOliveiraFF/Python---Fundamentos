#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente.
import math
angulo = float(input('Digite um ângulo:'))
anguloRad = math.radians(angulo)
sen = math.sin(anguloRad)
cos = math.cos(anguloRad)
tang = math.tan(anguloRad)
print('O ângulo {} possui SENO {:.2f}, COSSENO {:.2f} e TANGENTE {:.2f}!'.format(angulo, sen, cos, tang))
