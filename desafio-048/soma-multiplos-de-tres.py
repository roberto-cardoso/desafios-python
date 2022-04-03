soma = 0
cont = 0
for c in range (1, 501, 2):
    if c % 3 == 0:
        soma += c
        cont += 1
print('-=-='*15)
print('O somatório de todos os \033[34m{}\033[m valores solicitados é: \033[34m{}\033[m.'.format(cont, soma))
print('-=-='*15)