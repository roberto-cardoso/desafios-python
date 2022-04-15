total = total1000 = menor = cont = 0
barato = ' '
while True:
    produto = str(input('Nome do produto: '))
    preço = float(input('Preço: R$ '))
    cont += 1
    total += 1
    if preço > 1000:
        total1000 += 1
    if cont == 1 or preço < menor:
        menor = preço
        barato = produto
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if resp == 'N':
        break
print('{:-^40}'.format(' FIM DO PROGRAMA '))
print('O total da compra foi R${:.2f}'.format(total))
print('Temos {} produtos custando mais de R$1000,00.'.format(total1000))
print('O produto mais barato foi {} que custa {}'.format(barato, menor))
