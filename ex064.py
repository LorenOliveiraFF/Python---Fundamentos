# Crie um programa que leia vários números inteiros pelo teclado.
# O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
# No final, mostre quantos números foram digitados e qual foi a soma entre eles

soma = 0
numero = 0
contador = 0
semflag = 0
while numero != 999:
    numero = int(input('Digite um número [999 para parar]:'))
    soma += numero
    semflag = soma - 999
    contador += 1
contador = contador - 1
print('Você digitou {} números e a soma entre eles foi {}!'.format(contador, semflag))
