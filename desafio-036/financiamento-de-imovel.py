print("=== O banco vai liberar ou não o empréstimo? ===")

casa = float(input("Qual o valor da casa? R$"))
salario = float(input("Quanto recebe o futuro comprador?"))
anos = int(input("Em quantos anos a casa será paga?"))
prestacao = casa / (anos*12)
trinta_porcento = salario*0.3

if prestacao <= trinta_porcento:
    print("===========")
    print("\033[32mEmpréstimo APROVADO!\033[m")
    print(f"Para pagar esse imóvel de R$\033[33m{casa:.2f}\033[m em \033[33m{anos}\033[m anos, a parcela será de R$\033[33m{prestacao:.2f}\033[m")
else:
    print("===========")
    print("\033[31mEmpréstimo NEGADO\033[m!")
print("=== FIM ===")
