n = str(input("Digite seu nome completo: ")).title().strip()
nome = n.split()
print(f"Analisando seu nome...")
print(f"Seu primeiro nome é: {nome[0]}")
print(f"Seu último nome é: {nome[len(nome)-1]}")