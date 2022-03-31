from random import randint
from time import sleep
itens = ('pedra', 'papel', 'tesoura')
computador = randint(0, 2)
print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogador = int(input('Qual é a sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
print('-='*12)
print('Computador jogou {}'.format(itens[computador]))
print('Jogador jogou {}'.format(itens[jogador]))
print('-='*12)
if computador == 0: #pedra
    if jogador == 0:
        print('Empatou')
    elif jogador == 1:
        print('\033[32mJogador venceu!')
    elif jogador == 2:
        print('\033[31mComputador venceu!')
    else:
        print('JOGADA INVÁLIDA!')
elif computador == 1: #papel
    if jogador == 0:
        print('\033[31mComputador venceu!')
    elif jogador == 1:
        print('Empatou')
    elif jogador == 2:
        print('\033[32mJogador venceu!')
    else:
        print('JOGADA INVÁLIDA!')
elif computador == 2: #tesoura
    if jogador == 0:
        print('\033[32mJogador venceu!')
    elif jogador == 1:
        print('\033[31mComputador venceu!')
    elif jogador == 2:
        print('Empatou')
    else:
        print('JOGADA INVÁLIDA!')
