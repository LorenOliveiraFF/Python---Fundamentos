# Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci.
print('-' * 25)
print('Sequência de Fibonacci')
print('-' * 25)
termos = int(input('Quantos termos você quer mostrar? '))
if termos == 1:
    print('0')
else:
    contador = 3
    t1 = 0
    t2 = 1
    print('{} -> {} -> '.format(t1, t2), end='')
    while contador <= termos:
        t3 = t1 + t2
        print(t3, '->', end=' ')
        t1 = t2
        t2 = t3
        contador += 1
print('Fim!', end='')
