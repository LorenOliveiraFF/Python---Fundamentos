# Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
# Guarde esses resultados em um dicionário em Python.
# No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.

from random import randint
from time import sleep
from operator import itemgetter

jogador = dict()
print('=*' * 20)
print(f'{"JOGO VALORES SORTEADOS":^35}')
print('=*' * 20)
for c in range(1, 5):
    jogador[f'Jogador{c}'] = randint(1, 6)

for jog, values in jogador.items():
    sleep(1)
    print(f'{jog} tirou {values} no dado!')

sleep(2)
print('=*' * 20)
print(f' {">>> RANKING DE JOGADORES <<<":^35}')
print('=*' * 20)

ranking = []
rank = sorted(jogador.items(), key=itemgetter(1), reverse=True)
for i, v in enumerate(rank):
    print(f'{i + 1} lugar: {v[0]} com dado {v[1]}!')
sleep(1)
