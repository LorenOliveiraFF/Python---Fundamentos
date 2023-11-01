#Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
#No final, mostre qual foi o maior e o menor valor digitado, e as posições.

posicaomaior = []
posicaomenor = []
valores = []

for c in range(0, 5):
    valores.append(int(input('Digite um número:')))

maior = menor = valores[0]

for valor in valores:
    if valor > maior:
        maior = valor
        print(maior)
    elif valor < menor:
        menor = valor
        print(menor)

for y, z in enumerate(valores):
    print('Maior:', maior)
    print('Menor:', menor)
    print('Y:', y)
    print('Z:', z)
    if maior == valores[y]:
        posicaomaior.append(y + 1)
        print('Entrei maior:', posicaomaior)
    if menor == valores[y]:
        posicaomenor.append(y + 1)
        print('Entrei menor:', posicaomenor)
print('A lista é:', valores)
print(f'O maior valor será de: {max(valores)} e está na posição {posicaomaior}.')
print(f'O menor valor será de: {min(valores)} e está na posição {posicaomenor}.')
