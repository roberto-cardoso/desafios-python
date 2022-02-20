from datetime import date

print("------Alistamento Militar ------")

ano = int(input("Ano de nascimento: "))
idade = date.today().year - ano

print(f"Quem nasceu em {ano} tem {idade} anos em {date.today().year}.")

if idade == 18:
    
    print("Você deve se alistar IMEDIATAMENTE!")

elif idade > 18:
    print(f"Você já deveria ter se alistado há {idade - 18} anos.")
    print(f"Seu alistamento foi em {date.today().year - (idade - 18)}.")

else:
    print(f"Ainda faltam {18 - idade} anos para o alistamento.")
    print(f"Seu alistamento será em {date.today().year - (idade - 18)}.")
    
print("------ FIM ------")
