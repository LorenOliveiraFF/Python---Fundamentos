nome = input('Digite o nome completo:').title().strip()
verif = 'Silva' in nome
print('Seu nome tem Silva?', verif)

#ou
print('Seu nome tem Silva? {}'.format('Silva' in nome))
