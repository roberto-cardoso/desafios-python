n1 = int(input("Digite um valor inteiro: "))
n2 = int(input("Agora digite outro valor: "))
n3 = int(input("Agora outro: "))
menor = n1
if n2<n1 and n2<n3:
    menor = n2
if n3<n1 and n3<n2:
    menor = n3
maior = n1
if n2>n1 and n2>n3:
    maior = n2
if n3>n1 and n3>n2:
    maior = n3
print(f"O maior número digitado foi {maior}.")
print(f"e o menor número digitado foi {menor}.")
