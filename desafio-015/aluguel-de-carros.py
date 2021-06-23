print("-"*35)

dias = int(input('Quantos dias o carro ficou alugado?'))
km = float(input('Quantos quilômetros ele andou?'))

print('O valor a ser pago é de R${:.2f}.'.format(dias*60+km*0.15))

print("-"*35)