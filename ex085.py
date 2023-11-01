# Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que
# mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.

numeros = [[], []]
for num in range(1, 8):
    escolhanumero = int(input(f'Digite o {num}ª valor: '))
    if escolhanumero % 2 == 0:
        numeros[0].append(escolhanumero)
    else:
        numeros[1].append(escolhanumero)

print('Pares:', sorted(numeros[0]))
print('Impares:', sorted(numeros[1]))
