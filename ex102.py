# Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique o número
# a calcular, e outro chamado show, que será um valor lógico (opcional) indicando se será mostrado
# ou não na tela o processo de cálculo do fatorial.

def fatorial(num, show=False):
    """
    > Calcula o Fatorial de um número.
    :param num: O número a ser calculado.
    :param show: (opcional) Mostrar ou não a conta.
    :return: O valor do fatorial de um número n.
    """
    if show:
        count = num-1
        print(f'{num} x', end=' ')
        while count > 0:
            print(f'{count} x ' if count > 1 else f'{count} = ', end='')
            num *= count
            count -= 1
        print(num)
    else:
        count = num - 1
        while count > 0:
            num *= count
            count -= 1
        print(num)


fatorial(6, True)
help(fatorial)