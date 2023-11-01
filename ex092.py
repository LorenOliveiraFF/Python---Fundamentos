# Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário.
# Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário.
# Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.

dados = dict()
dados['nome'] = input('Nome: ')
dados['anonasc'] = int(input('Ano Nascimento: '))
idade = 2023 - dados['anonasc']
dados['idade'] = idade
dados['carteira'] = int(input('Carteira de Trabalho (0 não tem!): '))
if dados['carteira'] == 0:
    print(f'Nome é: {dados["nome"]}!')
    print(f'Tem {dados["idade"]} anos!')
    print(f'CTPS tem valor {dados["carteira"]}!')
else:
    dados['contratacao'] = int(input('Ano de Contratação: '))
    dados['salario'] = float(input('Salário: R$ '))
    anoaposent = dados['contratacao'] - dados['anonasc']
    dados['idadeaposent'] = anoaposent + 30
    print(f'Nome é: {dados["nome"]}!')
    print(f'Tem {dados["idade"]} anos!')
    print(f'CTPS tem valor {dados["carteira"]}!')
    print(f'Contratação tem o ano de: {dados["contratacao"]}')
    print(f'Salário tem o valor de R${dados["salario"]}')
    print(f'Aposentadoria será com {dados["idadeaposent"]} anos!')
