# Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.

numero = int(input('Digite um número:'))
for c in range(1, 11):
    tabuada = (numero * c)
    print(numero, ' x ', c, '=', tabuada)
print('Fim!')

#OU
numero = int(input('Digite o número para ver a sua tabuada:'))
for c in range(1, 11):
    print(numero, 'x', c, '=', numero*c)
