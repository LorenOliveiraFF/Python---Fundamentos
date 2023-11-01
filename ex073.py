# Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol,
# na ordem de colocação. Depois mostre:
# a) Os 5 primeiros times.
# b) Os últimos 4 colocados.
# c) Times em ordem alfabética.
# d) Em que posição está o time que o usuário deseja saber.

classif = ('Botafogo', 'Bragantino', 'Grêmio', 'Palmeiras', 'Flamengo', 'Fortaleza', 'Fluminense',
           'AthleticoPR', 'AtléticoMG', 'São Paulo', 'Cuiabá', 'Internacional', 'Corinthians', 'Santos',
           'Cruzeiro', 'Bahia', 'Vasco da Gama', 'Goiás', 'Coritiba', 'América-MG')


print('*' * 175)
print(f'Lista de times do Brasileirão: {classif}')
print('*' * 175)
print(f'Os 5 primeiros são {classif[0:5]}.')
print('*' * 175)
print(f'Os 4 últimos são {classif[-4:]}.')
print('*' * 175)
print(f'Times em ordem alfabética: {sorted(classif)}.')
print('*' * 175)
nometime = input('Qual time você deseja saber a posição: ').strip().capitalize()
while nometime not in classif:
    nometime = input('Qual time você deseja saber a posição: ').strip().capitalize()
posicaotime = classif.index(nometime)
print(f'O {nometime} está na {posicaotime + 1}ª posição.')
