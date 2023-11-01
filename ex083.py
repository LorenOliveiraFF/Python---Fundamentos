# Crie um programa onde o usuário digite uma expressão qualquer que use parênteses.
# Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.

#SEM LISTA
opc = 'S'
contaparentesesaberto = contaparentesesfechado = 0
while opc in 'Ss':
    usuario = input('Digite uma expressão matemática: ')
    contaparentesesaberto = usuario.count('(')
    contaparentesesfechado = usuario.count(')')
    if contaparentesesaberto == contaparentesesfechado:
        print('Expressão matemática feita corretamente!')
    else:
        print('Expressão matemática inválida!')
    opc = input('Quer continuar? [S/ N]: ')
    while opc not in 'SsNn':
        opc = input('Valor inválido! Quer continuar? [S/ N]: ')

# PILHA
exp = str(input('Digite a expressão:'))
lista = []
for item in exp:
    if item == '(':
        lista.append('(')
        print('Lista após APPEND aberto', lista)
    elif item == ')':
        if len(lista) > 0:
            lista.pop()
            print('Lista após POP:', lista)
        else:
            lista.append(')')
            print('Lista após APPEND fechado', lista)
            break
if len(lista) == 0:
    print('Operação correta!')
else:
    print('Operação incorreta!')
