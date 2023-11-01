# Tabuada 3.0
# Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor
# Digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.

contador = 1
while True:
    valor = int(input('Quer ver a tabuada de qual valor? '))
    contador = 1
    if valor < 0:
        print('Programa encerrado! Volte sempre!')
        break
    while contador <= 10:
        tabuada = valor * contador
        print(f'{valor} x {contador} = {tabuada}')
        contador += 1
