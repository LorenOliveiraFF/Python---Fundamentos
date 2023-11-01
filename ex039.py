# Faça um programa que leia o ano de nascimento de um jovem e informe, conforme a sua idade,
# se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento.
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
import datetime

nascimento = int(input('Digite o ano de nascimento:'))
ano = datetime.datetime.now().year
idade = ano - nascimento
print('Quem nasceu em {} tem {} anos em {}'.format(nascimento, idade, ano))
if idade == 18:
    print('Você tem que se alistar IMEDIATAMENTE!')
elif idade > 18:
    alist = idade - 18
    dataalist = ano - alist
    print('Você deveria ter se alistado há {} anos'.format(alist))
    print('Seu alistamento foi em {}'.format(dataalist))
else:
    alist = 18 - idade
    dataalist = ano + alist
    print('Ainda faltam {} ano(s) para o alistamento!'.format(alist))
    print('Seu alistamento será em {}'.format(dataalist))
