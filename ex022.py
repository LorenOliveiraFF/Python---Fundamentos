# Crie um programa que leia o nome completo de uma pessoa e mostre:
# O nome com todas as letras maiúsculas
# O nome com todas as letras minúsculas
# Quantas letras ao total (sem considerar espaços)
# Quantas letras tem o primeiro nome
nome = input('Digite o nome completo:')
maiuscula = nome.upper()
print(maiuscula)

minuscula = nome.lower()
print(minuscula)

qtdletras = nome.split()
qtdletras = ''.join(qtdletras)
print('O tamanho total é:', len(qtdletras))

primeironome = nome.split()
tamanho = len(primeironome[0])
print('Tamanho do primeiro nome:', tamanho)
