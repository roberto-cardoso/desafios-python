nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
média = (nota1 + nota2) / 2
print(f'Tirando {nota1:.1f} e {nota2:.1f}, a média do aluno é {média:.1f}')
if média >= 7:
    print('O aluno está \033[32maprovado\033[m.')
elif 7 > média >= 5:
    print('O aluno está de \033[33mrecuperação\033[m.')
else:
    print('O aluno está \033[31mreprovado\033[m.')
 