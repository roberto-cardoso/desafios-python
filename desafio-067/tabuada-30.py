numero = 0
while True:
    print('-=' * 23)
    numero = int(input('Qual número você gostaria de saber a tabuada? '))
    print('=-' * 23)
    if numero < 0:
            break
    for c in range(1, 11):
        mult = numero * c
        print('{} x {} = {}'.format(numero, c, mult))
print('Programa de tabuada encerrado.')
