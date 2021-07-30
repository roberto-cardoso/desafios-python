from datetime import date
print("=== Descubra se o ano é bissexto ou não ===")
ano = int(input("Digite o ano que gostaria de saber se é bissexto ou não ou digite 0 para saber sobre o ano atual: "))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f"O ano {ano} é bissexto.")
else:
    print(f"O ano {ano} não é bissexto.")
print("=== FIM ===")
