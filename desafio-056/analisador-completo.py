from re import I


somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = ''
totalmulher20 = 0

for p in range(1, 5):
    print('----- {}ª PESSOA -----'.format(p))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo: [M/F]: ')).strip().upper()
    somaidade += idade

    if p == 1 and sexo in 'M':
        maioridadehomem = idade
        nomevelho = nome

    if sexo in 'M' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome

    if sexo in 'F' and idade < 20:
        totalmulher20 += 1

mediaidade = somaidade / 4
print('A média de idade do grupo é de {} anos'.format(mediaidade))
print('O homem mais velho é o {} e ele tem {} anos de idade'.format(nomevelho, maioridadehomem))
print('Ao todo são {} mulheres com menos de 20 anos'.format(totalmulher20))
