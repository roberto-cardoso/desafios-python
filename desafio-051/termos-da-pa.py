print('='*17)
print('TERMOS DE UMA PA')
print('='*17)
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
decimo = primeiro + (10-1) * razao
for c in range(primeiro, decimo + razao, razao):
    print('{}'.format(c), end='⇉ ')
print('FIM')