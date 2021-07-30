import random

nj = int(input("Escolha um número inteiro de 0 até 5: "))
nc = random.randint(0, 5)

if nj == nc:
    print("Você acertou!! Parabéns!!")
else:
    print(f"Pééééééhhh! Você errou! A máquina escolheu {nc}!")
print("------FIM------")
