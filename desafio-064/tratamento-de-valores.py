numero = cont = soma = 0
numero = int(input('Digite um número [ou 999 para parar o programa]: '))
while numero != 999:    
    soma += numero
    cont += 1
    numero = int(input('Digite um número [ou 999 para parar o programa]: '))
print('Você digitou {} números e a soma deles é {}.'.format(cont, soma))
print('FIM')
