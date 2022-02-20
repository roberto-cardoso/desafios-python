peso = float(input('Qual o seu peso em Kg? '))
altura = float(input('Qual a sua altura em metros? '))
imc = peso / (altura ** 2)
if imc < 18.5:
    print(f'Seu IMC é {imc:.1f} e você está abaixo do seu peso ideal.')
elif imc <=25:
    print(f'Seu IMC é {imc:.1f} e você está no seu peso ideal.')
elif imc <= 30:
    print(f'Seu IMC é {imc:.1f} e você está com sobrepeso.')
elif imc <= 40:
    print(f'Seu IMC é {imc:.1f} e você tem obesidade.')
else:
    print(f'Seu IMC é {imc:.1f} e você tem obesidade mórbida.')
