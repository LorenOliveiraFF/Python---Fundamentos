#Faça um mini-sistema que utilize o Interactive Help do Python. O usuário vai digitar o comando e o manual vai aparecer.
# Quando o usuário digitar a palavra ‘FIM’, o programa se encerrará. Importante: use cores.
from time import sleep


#Programa Principal
comando = ''
while True:
    print('\033[0:30:42m~\033[m' * len('SISTEMA DE AJUDA PYHELP'))
    print('\033[0:30:42mSISTEMA DE AJUDA PYHELP\033[m')
    print('\033[0:30:42m~\033[m' * len('SISTEMA DE AJUDA PYHELP'))
    comando = str(input('Função ou Biblioteca: '))
    if comando.upper() == 'FIM':
        print('\033[0:30:41m~\033[m' * len('ATÉ LOGO!'))
        print('\033[0:30:41mATÉ LOGO!\033[m')
        print('\033[0:30:41m~\033[m' * len('ATÉ LOGO!'))
        break
    else:
        manual = f'ACESSANDO O MANUAL DO COMANDO {comando}'
        print('\033[0:30:44m~\033[m' * len(manual))
        print(f'\033[0:30:44mACESSANDO O MANUAL DO COMANDO {comando.upper()}\033[m')
        print('\033[0:30:44m~\033[m' * len(manual))
        sleep(2)
        help(comando)
