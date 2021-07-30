salario = float(input("Digite o salário do funcionário: R$"))
if salario <= 1250:
    print(f"O novo salário desse funcionário será R${salario+(salario*0.15)}")
else:
    print(f"O novo salário desse funcionário será R${salario+(salario*0.1)}")
