#Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
#Faça um programa que ajude ele, lendo o nome e escrevendo o nome escolhido.
import random

a1 = str(input('Primeiro aluno:'))
a2 = str(input('Segundo aluno:'))
a3 = str(input('Terceiro aluno:'))
a4 = str(input('Quarto aluno:'))
sorteio = random.choice([a1, a2, a3, a4])
print('O aluno sorteado foi o(a) {}!'.format(sorteio))

#PROGRAMA MEGASENA
x = str(random.sample(range(1, 60), 6))
colchOne = x.replace('[', '')
print(colchOne.replace(']', ''))
#REPLACE serve para tirar uma STRING do resultado.

sorteiorange = random.randrange(1, 40)
print(sorteiorange)

