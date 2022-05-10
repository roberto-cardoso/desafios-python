listagem = ('Lápis', 1.75,
            'Borracha', 2,
            'Caderno', 15.90,
            'Estojo', 25,
            'Transferidor', 4.20,
            'Compasso', 9.99,
            'Mochila', 120.32,
            'Canetas', 22.30,
            'Livro', 34.90)
print('-' * 40)
print('{:^40}'.format("Listagem de Preços"))
print('-' * 40)
for item in range(0, len(listagem)):
    if item % 2 ==0:
        print('{:.<30}'.format(listagem[item]), end='')
    else:
        print('R${:>7.2f}'.format(listagem[item]))
print('-' * 40)
