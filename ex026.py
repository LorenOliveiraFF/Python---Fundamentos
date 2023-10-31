frase = str(input('Digite uma frase:')).strip().lower()
letra = input('De qual letra você quer saber as informações?').strip().lower()
qtdletra = frase.count(letra)
posicletra = frase.find(letra)+1
ultiletra = frase.rfind(letra)+1
print('A letra {} apareceu {} vez(es) na frase!'.format(letra, qtdletra))
print('A primeira letra {} apareceu na posição {}'.format(letra, posicletra))
print('A última letra {} apareceu na posição {}'.format(letra, ultiletra))