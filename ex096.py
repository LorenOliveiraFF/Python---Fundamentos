# Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular
# (largura e comprimento) e mostre a área do terreno.

print('Controles de Terrenos')
print('=*' * 11)


def area(l, c):
    ar = l * c
    print(f'A área de um terreno {l}x{c} é de {ar}m²!')


larg = float(input('LARGURA (m): '))
comp = float(input('COMPRIMENTO (m): '))
area(larg, comp)
