#Faça um programa que leia um ano qualquer e mostre se ele é bissexto.
import datetime

ano = int(input('Digite qual ano quer analisar! Digite 0 para analisar o ano atual! Ano:'))
if ano == 0:
    ano = datetime.datetime.now().year

anoDiv4 = ano % 4
anoDif100 = ano % 100
if anoDiv4 == 0 and anoDif100 != 0:
    print('{} é um ano Bissexto!'.format(ano))
else:
    print('{} não é um ano Bissexto!'.format(ano))
