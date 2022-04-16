numeros = (int(input('Digite um número: ')),
           int(input('Digite mais um número: ')), 
           int(input('Digite outro número: ')), 
           int(input('Agora é sério, o último: ')))
print('Você digitou os valores {}'.format(numeros))
print('O número 9 apareceu {} vezes'.format(numeros.count(9)))
if 3 in numeros:
    print('O número 3 apareceu na {}ª posição'.format(numeros.index(3) + 1))
else:
    print('O valor 3 não foi digitado.')    
print('Os valores pares digitados foram ', end='')
for n in numeros:
    if n % 2 == 0:
        print(n, end=' ')
                                                