# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
# No final do programa, mostre: a média de idade do grupo,
# qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.

mulhervinte = 0
maioridade = 0
nomevelho = ''
somaIdade = 0
numPessoa = 0

for pessoa in range(1, 5):
    print('----- {}ª PESSOA -----'.format(pessoa))
    nome = input('Nome:')
    idade = int(input('Idade:'))
    sexo = input('Sexo [M/F]:')
    somaIdade += idade
    numPessoa = pessoa
    if sexo in 'Ff' and idade < 20:
        mulhervinte += 1
    elif sexo in 'Mm' and idade > maioridade:
        maioridade = idade
        nomevelho = nome

mediaidade = somaIdade / numPessoa
print('A média de idade do grupo é de: {}'.format(mediaidade))

print('O homem mais velho tem {} anos e se chama {}'.format(maioridade, nomevelho))

print('Ao todo são {} mulheres com menos de 20 anos!'.format(mulhervinte))
