print('-=' * 20)
print('TUPLA - NÚMEROS TUPLA')
print('-=' * 20)
par = ''
num = (int(input('Digite o 1º número: ')), int(input('Digite o 2º número: ')), int(input('Digite o 3º número: ')),
       int(input('Digite o 4º número: ')))
print(num)
print(f'o número 9 foi digitado {num.count(9)} vezes.')
if 3 in num:
    print(f'O número 3 aparece na {num.index(3) + 1}ª posição.')
else:
    print('O número 3 não foi digitado')
print('Os números pares digitados foram: ', end='')
for c in num:
    if c % 2 == 0:
        par = c
        print(par, end=' ')
if par == '':
    print('Nenhum')
print('\nFIM')
