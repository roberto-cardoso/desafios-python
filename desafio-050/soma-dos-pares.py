soma = 0
cont = 0
for n in range (1, 7):
    num = int(input('Digite o {} valor: '.format(n)))
    if num % 2 == 0:
        soma += num
        cont += 1
print('Você informou {} número(s) \033[32mpar(es)\033[m e a soma foi \033[32m{}\033[m.'.format(cont, soma))
