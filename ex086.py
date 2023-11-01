#Crie um programa que declare uma matriz de dimensão 3×3 e preencha com valores lidos pelo teclado.
# No final, mostre a matriz na tela, com a formatação correta.

matriz = [[], [], []]
for a in range(0, 3):
    for b in range(0, 3):
        num = int(input(f'Digite um número [{a}, {b}]:'))
        matriz[a].append(num)

print(f'[{matriz[0][0]:^5}][{matriz[0][1]:^5}][{matriz[0][2]:^5}]')
print(f'[{matriz[1][0]:^5}][{matriz[1][1]:^5}][{matriz[1][2]:^5}]')
print(f'[{matriz[2][0]:^5}][{matriz[2][1]:^5}][{matriz[2][2]:^5}]')

#OUTRA POSSIBILIDADE:
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for a in range(0, 3):
    for b in range(0, 3):
        matriz[a][b] = int(input(f'Digite um número [{a}, {b}]:'))

for a in range(0, 3):
    for b in range(0, 3):
        print(f'[{matriz[a][b]:^5}]', end='')
    print()
