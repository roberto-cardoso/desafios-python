from random import randint
computador = randint(0, 10)
print('=-=-=-=-=-=-= Jogo da adivinhação =-=-=-=-=-=-=')
print('Eu sou o seu computador, acabei de pensar em um número e duvido você adivinhar qual é.')
acertou = False
palpite = 0
while not acertou:
    jogador = int(input('Chuta aí um número: '))
    palpite += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... Tenta de novo')
        elif jogador > computador:
            print('Menos... Chuta de novo')
if palpite == 1:
    print('Parabéns por acertar de primeira!!')
else:
    print('Só acertou depois de {} tentativas então não merece meus parabéns.'.format(palpite))
print('=-=-=-=-=-=-= Fim do jogo =-=-=-=-=-=-=')
