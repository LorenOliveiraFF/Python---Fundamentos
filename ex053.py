#Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.

frase = str(input('Digite uma frase: '))
frasejunto = ''.join(frase.split())
fraseinversa = []
tamanho = len(frasejunto)

for c in range(tamanho, 0, -1):
    fraseinversa.append(frasejunto[c-1])

frasefinal = ''.join(fraseinversa)
print(frasefinal)
if frasejunto.lower() == frasefinal.lower():
    print('É um palíndromo!')
else:
    print('Não é um palíndromo!')

# -----
frase = str(input('Digite uma frase:')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) -1, -1, -1):
    inverso += junto[letra]
if inverso == junto:
    print('Temos um palíndromo!')
else:
    print('A frase não é um palíndromo!')

# --------
frase = str(input('Digite uma frase:')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = junto[::-1]
print('O inverso de {} é {}'.format(junto, inverso))
if inverso == junto:
    print('Temos um palíndromo!')
else:
    print('A frase não é um palíndromo!')




