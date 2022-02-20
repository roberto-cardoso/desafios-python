print('=== Descubra se um triângulo é possível ===')
reta1 = float(input('Digite o valor da primeira reta: '))
reta2 = float(input('Digite o valor da segunda reta: '))
reta3 = float(input('Digite o valor da terceira reta: '))
maior = reta1
if reta1 < reta2 + reta3 and reta2 < reta1 + reta3 and reta3 < reta1 + reta2:
    print('Estes segmentos de reta formam um triângulo ', end='')
    if reta1 == reta2 == reta3:
        print('Equilátero.')
    elif reta1 != reta2 != reta3 != reta1:
        print('Escaleno.')
    else:
        print('Isósceles.')
else:
    print('Este triângulo não é possível!')
print('=== FIM ===')
