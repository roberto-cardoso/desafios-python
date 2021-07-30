print("=== Descubra se um triângulo é possível ===")
reta1 = float(input("Digite o valor da primeira reta: "))
reta2 = float(input("Digite o valor da segunda reta: "))
reta3 = float(input("Digite o valor da terceira reta: "))
maior = reta1
if reta1 < reta2 + reta3 and reta2 < reta1 + reta3 and reta3 < reta1 + reta2:
    print("Este triângulo é possível!")
else:
    print("Este triângulo não é possível!")
print("=== FIM ===")
