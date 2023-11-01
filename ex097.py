# Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro
# e mostre uma mensagem com tamanho adaptável.
# Ex: escreva(‘Olá, Mundo!’)
# Saída:
# ~~~~~~~~~
# Olá, Mundo!
# ~~~~~~~~~
def escreva(txt):
    tamanho = len(txt)
    print('~' * (tamanho + 2))
    print(f' {txt} ')
    print('~' * (tamanho + 2))


escreva('Loren Oliveira')
escreva('Fernando')
escreva('Curso de Python no Youtube')
escreva('CeV')
