# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado.
# Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

km = float(input('Quantos km você percorreu com o carro?'))
dias = int(input('Quantos dias você ficou com o carro?'))
valorkm = km * 0.15
valordias = dias * 60
valorTotal = valorkm + valordias
print('O valor total do aluguel será de R${:.2f}'.format(valorTotal))