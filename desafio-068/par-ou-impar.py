from random import randint
v = 0
print('=-' * 15)
print('Jogo de Par ou Ímpar')
print('-=' * 15)
while True:
    jogador = int(input('Digite um valor entre 0 e 10: '))
    pc = randint(0, 11)
    total = jogador + pc
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Ímpar? [P/I] ')).strip().upper()[0]
    print('Você jogou {} e o computador jogou {}. Total de {}'.format(jogador, pc, total), end=' ')
    print('Deu Par' if total % 2 == 0 else 'Deu ímpar')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você venceu!')
            v += 1
        else:
            print('Você perdeu!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Você venceu!')
            v += 1
        else:
            print('Você perdeu!')
            break
    print('Vamos jogar de novo...')
print('GAME OVER! Você venceu {} vezes.'.format(v))
