print('-=' * 20)
print('LISTA - VALORES')
print('-=' * 20)
num = []
for n in range(0, 5):
    num.append(int(input('Digite um número: ')))
print(num)
print(f'O maior valor da lista é {max(num)} e sua posição na lista é ', end='')
for pos, n in enumerate(num):
    if n == max(num):
        print(f'{pos}...', end='')
print(f'\nO menor valor da lista é {min(num)} e sua posição na lista é ', end='')
for pos, n in enumerate(num):
    if n == min(num):
        print(f'{pos}...', end='')
print('\nFIM')
