# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
# – à vista dinheiro/cheque: 10% de desconto
# – à vista no cartão: 5% de desconto
# – em até 2x no cartão: preço formal
# – 3x ou mais no cartão: 20% de juros

print('=' * 8 + ' LOJINHA ' + '=' * 8)
compra = float(input('Valor da compra: R$'))
print('FORMAS DE PAGAMENTO:'
      '\n [1] à vista dinheiro/cheque'
      '\n [2] à vista no cartão'
      '\n [3] 2x no cartão'
      '\n [4] 3x ou mais no cartão')
opcao = int(input('Qual a sua opção?'))
if opcao == 1:
    valor = compra - (compra * 0.1)
    print('Com desconto de 10%, sua compra de R${:.2f} agora sairá por R${:.2f}'.format(compra, valor))
elif opcao == 2:
    valor = compra - (compra * 0.05)
    print('Com desconto de 5%, sua compra de R${:.2f} agora sairá por R${:.2f}'.format(compra, valor))
elif opcao == 3:
    print('O valor de sua compra não possui desconto e ficou em R${:.2f}'.format(compra))
elif opcao == 4:
    parcelas = int(input('Quantas parcelas?'))
    if parcelas < 3:
        print('Você inseriu um valor de parcela inválida nesta opção. Comece novamente!')
    else:
        valor = compra + (compra * 0.2)
        pagamento = valor / parcelas
        print('Sua compra será parcelada em {}x de R${:.2f} COM JUROS!'.format(parcelas, pagamento))
        print('Sua compra de R${:.2f} sairá por R${:.2f} no final.'.format(compra, valor))
else:
    print('Você digitou um valor inválido ou saiu do programa.')
