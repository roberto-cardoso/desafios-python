import math

print("="*40)

print("Calculando uma hipotenusa")
co = float(input("Qual o valor do cateto oposto? "))
ca = float(input("Qual o valor do cateto adjacente? "))
h1 = math.hypot(co, ca)

print("A hipotenusa desse triângulo vale {:.2f}".format(h1))

print("="*40)