# Crie um programa que gerencie o aproveitamento de um jogador de futebol.
# O programa vai ler o nome do jogador e quantas partidas ele jogou.
# Depois vai ler a quantidade de gols feitos em cada partida.
# No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.

dados = dict()
gols = []
somagols = 0
dados['nome'] = str(input('Nome Jogador: '))
partidas = int(input(f'Quantas partidas {dados["nome"]} jogou? '))
for c in range(0, partidas):
    qtdgols = int(input(f'Quantos gols na partida {c}? '))
    somagols += qtdgols
    gols.append(qtdgols)
dados['gols'] = gols
dados['total'] = somagols
print('=*' * 30)
print(dados)
print('=*' * 30)
print(f'O campo nome tem o valor {dados["nome"]}!')
print(f'O campo gols tem o valor {dados["gols"]}!')
print(f'O campo total tem o valor {dados["total"]}!')
print('=*' * 30)
print(f'O jogador {dados["nome"]} jogou {partidas} partidas!')
for cont in range(0, partidas):
    print(f' => Na partida {cont}, fez {dados["gols"][cont]} gols!')

print(f'Foi um total de {dados["total"]} gols!')
