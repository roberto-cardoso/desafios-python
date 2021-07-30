numero = int(input("Digite um número de 0 a 9999: "))
u = numero // 1 % 10
d = numero // 10 % 10
c = numero // 100 % 10
m = numero // 1000 % 10
print(f"Analisando este número {numero}...")
print(f"Unidade {u}")
print(f"Dezena{d}")
print(f"Centena{c}")
print(f"Milhar{m}")