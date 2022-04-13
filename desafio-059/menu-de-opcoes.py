from time import sleep
print('=-'*15)
numero1 = int(input('Digite um número: '))
numero2 = int(input('Digite outro número: '))
opcao = 0
while opcao != 5:
    print('''O que você quer fazer com esses números?
    [1] Somar
    [2] Multiplicar
    [3] Maior
    [4] Novos números
    [5] Sair do programa''')
    opcao = int(input('>>>> Sua opção é: '))
    if opcao == 1:
        print('{} + {} = {}'.format(numero1, numero2, numero1+numero2))
    elif opcao == 2:
        print('{} . {} = {}'.format(numero1, numero2, numero1*numero2))
    elif opcao == 3:
        if numero1 > numero2:
            maior = numero1
        else:
            maior = numero2
        print('O maior número é {}'.format(maior))
    elif opcao == 4:
        print('Preparando para receber os números novos....')
        sleep(2)
        numero1 = int(input('Digite um número: '))
        numero2 = int(input('Digite outro número: '))
    elif opcao ==5:
        print('Finalizando....')
    else:
        print('Digite uma opção válida')
    print('-='*15)
    sleep(2)
print('-=-=-=-=- Fim do programa -=-=-=-=-')