from random import randint
from time import sleep
lista = list()
jogos = list()
print('-' * 30)
print('      Joga na Mega Sena')
print('-' * 30)
quantidade = int(input('Quantos jogos você vai jogar: '))
total = 1
while total <= quantidade:
    cont = 0
    while True:
        numero = randint(1, 60)
        if numero not in lista:
            lista.append(numero)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    total += 1
print('-=' * 3, f'Sorteando {quantidade} jogos', '=-' * 3)
for i, l in enumerate(jogos):
    print(f'Jogo {i+1}: {l}')
    sleep(1)
print()
print('-=' *5, '< Boa sorte >', '=-' * 5)

