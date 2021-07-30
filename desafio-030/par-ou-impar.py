numero = int(input("Digite um número inteiro e descubra se ele é par ou ímpar: "))
resto = numero % 2
if resto == 0:
    print(f"O número {numero} é par.")
else:
    print(f"O número {numero} é impar.")
print("------FIM------")
