print("------ Comparador de números ------")

num1 = int(input("Digite um número: "))
num2 = int(input("Digite outro número: "))

if num1 > num2:
    print(f"O número \033[33m{num1}\033[m é maior.")
elif num1 < num2:
    print(f"O número \033[33m{num2}\033[m é maior")
else:
    print("Você digitou dois números iguais, bobão!")
    
print("------ FIM ------")
