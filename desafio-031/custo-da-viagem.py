print("--- Descubra o valor da passagem ---")
distancia = float(input("Digite a distância da viagem em km: "))
if distancia <= 200:
    print(f"Essa passagem custará R${distancia*0.5}")
else:
    print(f"Essa passagem custará R${distancia*0.45}")
print("--- Boa viagem! ;D ---")
