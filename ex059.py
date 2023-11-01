# Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela:
# [ 1 ] somar
# [ 2 ] multiplicar
# [ 3 ] maior
# [ 4 ] novos números
# [ 5 ] sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso.

from time import sleep

primeiro = int(input('Primeiro valor:'))
segundo = int(input('Segundo valor:'))
opcao = 0

while opcao != 5:
    print(' [1] Somar '
          '\n [2] Multiplicar '
          '\n [3] Maior '
          '\n [4] Novos Números '
          '\n [5] Sair')
    opcao = int(input('Qual a sua opção? '))
    if opcao == 1:
        soma = primeiro + segundo
        print('A soma entre {} e {} é {}.'.format(primeiro, segundo, soma))
        print('=' * 20)
    elif opcao == 2:
        multiplica = primeiro * segundo
        print('A multiplicação entre {} e {} é {}.'.format(primeiro, segundo, multiplica))
        print('=' * 20)
    elif opcao == 3:
        if primeiro > segundo:
            print('O maior número entre {} e {} é {}.'.format(primeiro, segundo, primeiro))
            print('=' * 20)
        else:
            print('O maior número entre {} e {} é {}.'.format(primeiro, segundo, segundo))
            print('=' * 20)
    elif opcao == 4:
        print('Informe os números novamente!')
        primeiro = int(input('Primeiro valor: '))
        segundo = int(input('Segundo valor: '))
    elif opcao <= 0 or opcao > 5:
        print('Opção inválida! Tente novamente!')
        print('=' * 20)
        sleep(2)
print('Finalizando o programa...')
sleep(2)
