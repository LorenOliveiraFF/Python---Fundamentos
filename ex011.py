# Faça um programa que leia a largura e a altura de uma parede em metros.
# Calcule sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m².

largura = float(input('Largura da Parede em M:'))
altura = float(input('Altura da Parede em M:'))
area = largura * altura
litros = area/2
print('A área da parede é de {}m², portanto serão necessários {} litros de tinta!'.format(area, litros))
