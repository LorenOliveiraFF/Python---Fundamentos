# Crie um programa que leia vários números inteiros pelo teclado.
# O programa só vai parar quando o usuário digitar 999, que é a condição de parada.
# No final, mostre quantos números foram digitados e qual foi a soma entre eles (sem flag).

contador = 0
soma = 0
while True:
    num = int(input('Digite um número: [999 para parar] '))
    if num == 999:
        break
    contador += 1
    soma += num
print(f'Foram digitados {contador} números e a soma entre eles deu {soma}!')
