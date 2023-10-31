# Desenvolva um programa que pergunte a distância de uma viagem em Km.
# Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.
dist = int(input('Qual a distância da sua viagem em km?'))
print('Você está prestes a começar uma viagem de {}km!'.format(dist))

#resolução Guanabara
preco = dist * 0.50 if dist <= 200 else dist * 0.45
print(preco)

#minha resolução
if dist <= 200:
    valor = dist * 0.50
else:
    valor = dist * 0.45
print('O preço da passagem é de R${:.2f}'.format(valor))
