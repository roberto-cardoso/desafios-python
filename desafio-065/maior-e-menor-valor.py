escolha = 'S'
quantidade = media = soma = maior = menor = 0
while escolha in 'S':
    numero = int(input('Digite um número: '))
    soma += numero
    quantidade += 1
    if quantidade == 1:
         maior = menor = numero
    else:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero
    escolha = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
media = soma / quantidade    
print('Você digitou {} números e a média foi {}'.format(quantidade, media))
print('O maior valor digitado foi {} e o menor foi {}'.format(maior, menor))