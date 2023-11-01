#Aprimore o desafio anterior, mostrando no final:
# A) A soma de todos os valores pares digitados.
# B) A soma dos valores da terceira coluna.
# C) O maior valor da segunda linha.

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for a in range(0, 3):
    for b in range(0, 3):
        matriz[a][b] = int(input(f'Digite um número [{a}, {b}]:'))
pares = 0
tercolun = 0
maior = 0
for a in range(0, 3):
    for b in range(0, 3):
        if matriz[a][b] % 2 == 0:
            pares += matriz[a][b]
        if b == 2:
            tercolun += matriz[a][b]
        print(f'[{matriz[a][b]:^5}]', end='')
        if a == 1:
            if b == 0:
                maior = matriz[a][b]
            elif b == 1:
                if matriz[a][b] > maior:
                    maior = matriz[a][b]
            else:
                if matriz[a][b] > maior:
                    maior = matriz[a][b]
    print()
print(f'A soma dos valores pares é {pares}!')
print(f'A soma dos valores da terceira coluna é {tercolun}!')
print(f'O maior valor da segunda linha é {maior}!')
