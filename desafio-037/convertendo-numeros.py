print("===== Conversor de bases numéricas =====")

numero = int(input("Digite um número inteiro: "))
print('''Escolha uma das bases para coverter seu número:
\033[36m[ 1 ]\033[m converte para \033[36mBINÁRIO\033[m
\033[35m[ 2 ]\033[m converte para \033[35mOCTAL\033[m
\033[33m[ 3 ]\033[m converte para \033[33mHEXADECIMAL\033[m''')
opcao = int(input("Sua opção: "))

if opcao == 1:
    print(f"\033[36m{numero}\033[m equivale a \033[36m{bin(numero)[2:]}\033[m em \033[36mBINÁRIO\033[m.")
elif opcao == 2:
    print(f"\033[35m{numero}\033[m equivale a \033[35m{oct(numero)[2:]}\033[m em \033[35mOCTAL\033[m.")
elif opcao == 3:
    print(f"\033[33m{numero}\033[m equvale a \033[33m{hex(numero)[2:]}\033[m em \033[33mHEXADECIMAL\033[m.")
else:
    print("Era pra escolher de 1 a 3, seu animal!")

print("===== FIM =====")