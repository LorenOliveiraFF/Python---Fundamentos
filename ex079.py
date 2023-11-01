# Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os
# em uma lista. Caso o número já exista lá dentro, ele não será adicionado.
# No final serão exibidos todos os valores únicos digitados, em ordem crescente.

valores = []
opc = 'S'
while opc == 'S' or opc == 's':
    num = int(input('Digite um valor: '))
    if num in valores:
        print('Valor duplicado! Não vou adicionar!')
    else:
        valores.append(num)
    opc = str(input('Quer continuar? [S/N]: '))
    while opc not in 'SsNn':
        opc = str(input('Inválido, tente novamente! Quer continuar? [S/N]: '))
print('*' * 50)
print(f'Você digitou os valores: {valores}')
