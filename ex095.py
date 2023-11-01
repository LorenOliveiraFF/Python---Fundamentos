# Crie um programa que gerencie o aproveitamento de um jogador de futebol.
# O programa vai ler o nome do jogador e quantas partidas ele jogou.
# Depois vai ler a quantidade de gols feitos em cada partida.
# No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.
# Aprimore o desafio 93 para que ele funcione com vários jogadores,
# Incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.

from time import sleep

dados = dict()
golsmarcados = []
lista = []
somagols = 0

opc = 'S'
while opc in 'Ss':
    dados['nome'] = str(input('Nome Jogador: '))
    partidas = int(input(f'Quantas partidas {dados["nome"]} jogou? '))
    for c in range(0, partidas):
        qtdgols = int(input(f'Quantos gols na partida {c}? '))
        somagols += qtdgols
        golsmarcados.append(qtdgols)
    dados['gols'] = golsmarcados
    dados['total'] = somagols
    lista.append(dados.copy())
    somagols = 0
    golsmarcados = []
    opc = str(input('Quer continuar? [S/ N]: '))
    while opc not in 'SsNn':
        print('Inválido! ', end='')
        opc = str(input('Quer continuar? [S/ N]: '))
print('=*' * 30)
print(f'COD {"NOME":>8} {"GOLS":>15} {"TOTAL":>26}')
print('=*' * 30)
for pos, val in enumerate(lista):
    print(f'{pos:<7} {lista[pos]["nome"]:<15} {str(lista[pos]["gols"]):<25} {lista[pos]["total"]}')
print('=*' * 30)

while True:
    ind = int(input('Mostrar dados de qual jogador? (999 para sair): '))
    if ind < len(lista):
        print(f'>>> LEVANTAMENTO DO JOGADOR {lista[ind]["nome"]}:')
        for k, v in enumerate(lista[ind]["gols"]):
            print(f'{"No":>6} jogo {k+1} fez {v} gols.')
    else:
        if ind == 999:
            print('ENCERRANDO...')
            sleep(1)
            print('>>> VOLTE SEMPRE <<<')
            break
        else:
            print(f'ERRO! Não existe jogador com o código {ind}!')
            print('=*' * 30)
