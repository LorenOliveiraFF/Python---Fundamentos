#Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
# Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

casa = float(input('Qual o valor da casa?'))
salario = float(input('Qual seu salário? R$'))
ano = int(input('Em quantos anos será o pagamento?'))
prestacao = casa / (ano * 12)
print('Para pagar uma casa de R${:.2f} em {} ano(s), a prestação será de R${:.2f}'.format(casa, ano, prestacao))
exced = (salario * 0.3)
if prestacao > exced:
    print('Empréstimo NEGADO!')
else:
    print('Empréstimo APROVADO!')
