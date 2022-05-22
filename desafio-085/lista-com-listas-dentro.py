numero = [[], []]
valor = 0

for c in range(1, 8):
    valor = int(input('Digite o {c}º valor: '))
    if valor % 2 == 0:
        numero[0].append(valor)
    else:
        numero[1].append(valor)

print('-=' * 30)
numero[0].sort()
numero[1].sort()
print(f'Todos os valores pares: {numero[0]}')
print(f'Todos os valores ímpares: {numero[1]}')
