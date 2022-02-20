preço = float(input('Qual o valor da compra? R$'))
fdp = int(input('Escolha a forma de pagamento \n[1] À vista no dinheiro/cheque \n[2] À vista no cartão \n[3] Em até 2 vezes no cartão \n[4] Em 3 vezes ou mais no cartão \n' ))
if fdp == 1:
    print(f'O valor terá 10% de desconto. O total a ser pago é R${preço - ((preço*10)/100):.2f}.')
elif fdp == 2:
    print(f'O valor terá 5% de desconto. O total a ser pago é R${preço - ((preço*5)/100):.2f}.')
elif fdp == 3:
    print(f'Nessa condição de pagamento não haverá descontos. O total a ser pago será R${preço:.2f}.')
elif fdp == 4:
    print(f'O valor terá um acréscimo de 20% de juros. O total a ser pago é R${preço + ((preço*20)/100)}')
else:
    print('Erro. Digite um número válido, idiota!!')
