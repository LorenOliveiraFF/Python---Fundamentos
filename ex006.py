#Crie um algoritmo que leia um número e mostre o dobro, triplo e a raiz quadrada.
numero = int(input('Digite um número:'))
dobro = numero * 2
triplo = numero * 3
raiz = numero ** (1/2)
raiz2 = pow(numero, (1/2))
print('Seu número foi: {}. '
      '\n O dobro é: {}. '
      '\n O triplo é: {}. '
      '\n A raiz quadrada é: {:.2f}.'.format(numero, dobro, triplo, raiz))

print('O outro jeito de ver raiz deu: {:.2f}.'.format(raiz2))