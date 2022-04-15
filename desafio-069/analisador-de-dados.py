total18 = totalm = totalm20 = 0
print('-=' * 10)
print('Cadastro de pessoas')
print('-=' * 10)
while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo [M/F]: ')).upper().strip()[0]
    if idade >= 18:
        total18 += 1
    if sexo == 'M':
        totalm += 1
    if sexo == 'F' and idade < 20:
        totalm20 += 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if resp == 'N':
        break
print('-=' * 20)
print('Total de pessoas com mais de 18 anos: {}'.format(total18))
print('Total de homens cadastrados: {}'.format(totalm))
print('Total de mulheres com menos de 20 anos: {}'.format(totalm20))
print('Fim do programa!')
print('-=' * 20)
