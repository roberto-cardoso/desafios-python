sexo = str(input('Informe o seu sexo: [M/F] ')).strip().upper()[0]
while sexo not in "MF":
    sexo = str(input('Deixa de ser idiota e digita certo! ')).strip().upper()[0]
print('Sexo {} registrado.'.format(sexo))
print('===Fim do programa===')