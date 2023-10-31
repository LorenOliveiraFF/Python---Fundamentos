#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
valorcarteira = int(input('Digite quantos R$ você possui na carteira:'))
valordolar = 5.05
podercompra = valorcarteira/valordolar
print('Hoje você poderá comprar US$ {:.2f} dólares!'.format(podercompra))
