import random

print("="*40)

print("Quem será o sortudo?")

a1 = str(input("Nome do(a) primeiro(a) aluno(a): "))
a2 = str(input("Nome do(a) segundo(a) aluno(a): "))
a3 = str(input("Nome do(a) terceiro(a) aluno(a): "))
a4 = str(input("Nome do(a) quarto(a) aluno(a): "))
lista = [a1,a2, a3, a4]

print("O sortudo(a) é o(a) {}.".format(random.choice(lista)))

print("="*40)