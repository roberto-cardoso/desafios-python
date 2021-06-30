import math

print("-"*40)

angulo = float(input("Informe o valor do ângulo de estudo: "))
sen = math.sin(math.radians(angulo))
cos = math.cos(math.radians(angulo))
tg = math.tan(math.radians(angulo))

print("Estes são os dados do ãngulo de {:.2f}:\n Seno: {:.2f}\n Cosseno: {:.2f}\n Tangente: {:.2f}".format(angulo, sen, cos, tg))

print("-"*40)