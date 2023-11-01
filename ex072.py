#Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso de zero até vinte.
#Seu programa deverá ler um número pelo teclado (0 e 20), e mostrá-lo por extenso.

extenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
opcUsuario = int(input('Digite um número entre 0 e 20: '))
while opcUsuario < 0 or opcUsuario > 20:
    opcUsuario = int(input('Opção inválida, tente novamente! Digite um número entre 0 e 20: '))
a = extenso[opcUsuario]
print(f'Você digitou o número {a}!')
