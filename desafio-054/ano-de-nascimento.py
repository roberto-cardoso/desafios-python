from datetime import date
atual = date.today().year
totalmaior = 0
totalmenor = 0
for pessoas in  range(1, 8):
    nascimento = int(input('Digite o ano de nascimento da {}ª pessoa: '.format(pessoas)))
    idade = atual - nascimento
    if idade >= 21:
        totalmaior += 1
    else:
        totalmenor += 1
print('Tivemos ao todo {} pessoas maiores de idade'. format(totalmaior))
print('e também tivemos um total de {} pessoas menores de idade.'.format(totalmenor))