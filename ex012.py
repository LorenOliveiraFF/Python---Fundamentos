#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço com 5% de desconto.
produto = float(input('Digite o valor do produto escolhido:'))
desconto = produto * 0.05
newvalor = produto - desconto
print('O valor do produto com desconto de 5% é de R${:.2f}'.format(newvalor))

