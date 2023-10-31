#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
salarioantigo = float(input('Qual o valor de salário atual?'))
aumento = salarioantigo * 0.15
salarioatual = salarioantigo + aumento
print('Seu antigo salário é de R${:.2f}, e o novo salário é de R${:.2f}'.format(salarioantigo, salarioatual))