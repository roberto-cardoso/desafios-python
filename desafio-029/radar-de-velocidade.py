v = float(input("Qual a velocidade do veículo? "))
if v <= 80:
    print("O veículo não recebeu multa pois estava dentro do limite.")
else:
    print(f"O veículo estava acima do limite permitido.\nSua multa será de R${(v-80)*7}.")
print("Excesso de velocidade pode causar acidentes. Seja prudente no trânsito.")
print("------FIM------")