palavras = ('aprender', 'programar', 'linguagem', 'python',
            'curso', 'gratis', 'estudar', 'praticar',
            'trabalhar', 'mercado', 'programador', 'futuro')
for p in palavras:
    print('\nNa palavra {} temos {}'.format(p, end=''))
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
