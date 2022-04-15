print('=' * 30)
print('{:^30}'.format("Betâo's Bank"))
print('=' * 30)
valor = int(input('Valor a ser sacado: R$'))
total = valor
cedula = 50
totalcedula = 0
while True:
    if total >= cedula:
        total -= cedula
        totalcedula += 1
    else:
        if totalcedula > 0:
            print('Total de {} cédulas de R${}'.format(totalcedula, cedula))
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        totalcedula = 0
        if total == 0:
            break
print('=' * 30)
print("Obrigado por usar o Betão's Bank")
