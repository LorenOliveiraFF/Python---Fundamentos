#Faça um programa que tenha uma função notas() que pode receber várias
# notas de alunos e vai retornar um dicionário com as seguintes informações:
# – Quantidade de notas
# – A maior nota
# – A menor nota
# – A média da turma
# – A situação (opcional)

def notas(*n, sit=False):
    """
    > Função para analisar notas e situações de vários alunos.
    :param n: Uma ou mais notas dos alunos (aceita várias)
    :param sit: Valor opcional, indicando se deve ou não adicionar a situação.
    :return: Dicionário com várias informações sobre a situação da turma.
    """
    dicionario = dict()
    soma = maior = menor = 0
    for p, v in enumerate(n):
        soma += v
        if p == 0:
            maior = menor = v
        else:
            if v >= maior:
                maior = v
            elif v <= menor:
                menor = v
    media = soma / len(n)
    situacao = ''
    dicionario = {
        'total': len(n),
        'maior': maior,
        'menor': menor,
        'media': f'{media:.2f}',
        'situação': situacao
    }
    if sit:
        if media < 5:
            dicionario['situação'] = 'RUIM!'
        elif 5 <= media <= 6:
            dicionario['situação'] = 'RAZOÁVEL!'
        else:
            dicionario['situação'] = 'BOA!'
    else:
        del dicionario['situação']
    return dicionario


# Programa Principal
result = notas(10, 6, 8.5)
print(result)
help(notas)