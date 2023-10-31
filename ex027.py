#Faça um programa que leia um nome completo, e informe o primeiro e o último nome.
nome = str(input('Digite o nome completo:')).strip()
nome = nome.split()
tamanho = len(nome)
print('Seu primeiro nome é {}'.format(nome[0]))
print('Seu último nome é {}'.format(nome[tamanho-1]))
