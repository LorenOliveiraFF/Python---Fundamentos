# Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros
# termos da progressão usando a estrutura while.

print('=' * 8, 'GERADOR DE PA', '=' * 8)
primeiro = int(input('Primeiro termo:'))
razao = int(input('Razão:'))
contador = 1
print(primeiro, '-> ', end='')
while contador < 10:
    primeiro = primeiro + razao
    contador += 1
    print(primeiro, '-> ',  end='')
print('Fim!')
