# Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros.
# Seu programa tem que analisar todos os valores e dizer qual deles é o maior.

def maior(*num):
    print('Analisando os valores passados...')
    print(f'Foram informados {len(num)} valores ao todo: {num}!')
    maiornum = 0
    for p, v in enumerate(num):
        if p == 0:
            maiornum = v
        else:
            if v > maiornum:
                maiornum = v
    print(f'O maior valor informado foi {maiornum}!')
    print('=*' * 25)


maior(1, 2, 5, 6, 7)
maior(1, 3)
maior(5, 6, 2, 8)
