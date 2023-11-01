# Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerrará quando ele disser que quer mostrar 0 termos.
print('=' * 8, 'GERADOR DE PA', '=' * 8)
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))

contador = 1
print(primeiro, '-> ', end='')
while contador < 10:
    primeiro = primeiro + razao
    contador += 1
    print(primeiro, '-> ',  end='')
print('PAUSA!')

qtdtermos = 1
armazenatermos = 0
cont = 1
somadostermos = 0

while qtdtermos > 0:
    qtdtermos = int(input('Quantos termos você quer mostrar a mais? '))
    armazenatermos = qtdtermos
    while cont <= armazenatermos:
        primeiro = primeiro + razao
        armazenatermos -= 1
        somadostermos += 1
        print(primeiro, '-> ',  end='')
    print('PAUSA!\n', end='')
print('Progressão finalizada com {} termos mostrados'.format(contador + somadostermos))
