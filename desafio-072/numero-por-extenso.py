contador = ('zero', 'um', 'dois', 'três', 'quatro',
          'cinco', 'seis', 'sete', 'oito', 'nove',
          'dez', 'onze', 'doze', 'treze', 'quatorze',
          'quinze', 'dezesseis', 'dezessete', 'dezoito',
          'dezenove', 'vinte')
while True:
    numero = int(input('Escolha um número de 0 até 20: '))
    if 0 <= numero <= 20:
        break
    print('Tente novamente.', end=' ')
print('Você digitou o número {}'.format(contador[numero]))
