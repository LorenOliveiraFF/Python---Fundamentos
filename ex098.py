# Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo.
# Seu programa tem que realizar três contagens através da função criada:
# a) de 1 até 10, de 1 em 1
# b) de 10 até 0, de 2 em 2
# c) uma contagem personalizada

from time import sleep


def contador(inicio, fim, passo):
    if inicio < fim:
        if passo == 0:
            print(f'Contagem de {inicio} até {fim} de {passo + 1} em {passo + 1}!')
            for cont in range(inicio, fim+1, 1):
                sleep(0.5)
                print(f'{cont} ', end='')
        else:
            print(f'Contagem de {inicio} até {fim} de {passo} em {passo}!')
            for cont in range(inicio, fim+1, passo):
                sleep(0.5)
                print(f'{cont} ', end='')
    if fim < inicio:
        if passo < 0:
            passoalterado = str(passo)
            print(f'Contagem de {inicio} até {fim} de {passoalterado.replace("-", "")} em {passo.alterado.replace("-", "")}!')
            for cont in range(inicio, fim-1, passo):
                sleep(0.5)
                print(f'{cont} ', end='')
        elif passo > 0:
            print(f'Contagem de {inicio} até {fim} de {passo} em {passo}!')
            for cont in range(inicio, fim-1, -passo):
                sleep(0.5)
                print(f'{cont} ', end='')
        elif passo == 0:
            print(f'Contagem de {inicio} até {fim} de {passo + 1} em {passo + 1}!')
            for cont in range(inicio, fim-1, -1):
                sleep(0.5)
                print(f'{cont} ', end='')
    print('Fim!', end='')
    print()


contador(1, 10, 1)
contador(10, 0, 2)
print('Agora é sua vez de personalizar a contagem!')
i = int(input('Inicio: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
contador(i, f, p)
