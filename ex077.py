print('-=' * 20)
print('TUPLA - VOGAIS')
print('-=' * 20)
palavras = ('casa', 'carro', 'moto', 'bicicleta', 'mula')
for c in palavras:
    print(f'\nNa palavra {c.upper()} as vogais são: ', end='')
    for vogal in c:
        if vogal in 'aeiou':
            print(vogal, end=' ')
print('\nFIM')
