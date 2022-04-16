from random import randint
tupla = (randint(1, 10), randint(1, 10), randint(1, 10),
         randint(1, 10), randint(1, 10), )
print('=-' *20)
print('Os números sorteados foram: {}'.format(tupla))
print('O maior valor é {} e o menor é {}'.format(max(tupla), (min(tupla))))
print('-=-=-=-=-=- Fim do programa -=-=-=-=-=-')