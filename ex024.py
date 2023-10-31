#Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com "santo", com True or False.
cid = str(input('Digite a cidade')).strip()
print(cid[:5].upper() == 'SANTO')

