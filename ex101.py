#Crie um programa que tenha uma função chamada voto() que vai receber como
# parâmetro o ano de nascimento de uma pessoa, retornando um valor literal
# indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.
from datetime import datetime


def voto(anonasc):
    anoatual = datetime.now().year
    idade = anoatual - anonasc
    resultado = ''
    if idade < 16:
        resultado = f'Com {idade} anos: VOTO NEGADO'
    elif 16 <= idade < 18 or idade >= 65:
        resultado = f'Com {idade} anos: VOTO OPCIONAL'
    else:
        resultado = f'Com {idade} anos: VOTO OBRIGATÓRIO'
    return resultado


nascimento = int(input('Ano de Nascimento: '))
a4 = voto(nascimento)
print(f'{a4}')
