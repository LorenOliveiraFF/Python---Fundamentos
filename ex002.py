#Inputs e concatenação.

nome = input('Digite seu nome:')
print('É um prazer te conhecer, ' + nome + '!')

nome = input('Digite seu nome:')
print('É um prazer te conhecer, {}!'.format(nome))

nome = input('Digite seu nome:')
idade = int(input('Quantos anos você tem?'))
print('É um prazer te conhecer, {}! Você tem {} anos!'.format(nome, idade))
