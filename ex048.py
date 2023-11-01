#Faça um programa que calcule a soma entre todos os números
# que são múltiplos de três e que se encontram no intervalo de 1 até 500.

count = 0
soma = 0
for c in range(0, 501, 3):
    if c % 2 == 1:
        count += 1
        soma += c
print('A soma de todos os {} valores apresentados é: {}'.format(count, soma))
