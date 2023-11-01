# Crie um Programa que leia a idade e o sexo de várias pessoas.
# A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar.
# No final, mostre:
# a) quantas pessoas tem mais de 18 anos
# b) quantos homens foram cadastrados
# c) quantas mulheres tem menos de 20 anos

continuidade = 'S'
contIdade = 0
contHomem = 0
contMulher = 0

while continuidade == 'S':
    print('-' * 20)
    print('CADASTRE UMA PESSOA')
    print('-' * 20)
    idade = int(input('Idade: '))
    sexo = ''
    while sexo != 'F' and sexo != 'M':
        sexo = input('Sexo [M/F]: ').strip().upper()
    if idade > 18:
        contIdade += 1
    if sexo == 'M':
        contHomem += 1
    if sexo == 'F' and idade < 20:
        contMulher += 1
    continuidade = str(input('Quer continuar [S/N]? ')).strip().upper()
    while continuidade != 'S' and continuidade != 'N':
        continuidade = str(input('Quer continuar [S/N]? '))
    if continuidade == 'N':
        break
print('===== FIM DO PROGRAMA =====')
print(f'Temos {contIdade} pessoas com mais de 18 anos!')
print(f'Ao todo temos {contHomem} homens cadastrados!')
print(f'Temos {contMulher} mulher(es) com menos de 20 anos!')
