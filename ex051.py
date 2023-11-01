# Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
# No final, mostre os 10 primeiros termos dessa progressão.

print('=' * 10)
print('10 TERMOS DE UMA PROGRESSÃO ARITMÉTICA')
print('=' * 10)
prim = int(input('Primeiro termo:'))
raz = int(input('Razão:'))
decimo = prim + (10-1) * raz
for c in range(prim, decimo + raz, raz):
    print(c, '-> ', end='')
print('ACABOU!')
