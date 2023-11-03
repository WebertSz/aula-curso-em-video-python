cores = {'limpa': '\033[m',
         'vermelho': '\033[1;31m',
         'verde': '\033[1;32m'}
print('-=' * 20)
print('LISTA - VÁRIOS NÚMEROS')
print('-=' * 20)
num = []
while True:
    num.append(int(input('Digite um número: ')))
    escolha = ' '
    while escolha not in 'SN':
        escolha = input('Deseja digitar outro número: [S/N]: ').strip().upper()
    if escolha == 'N':
        break
tam = len(num)
cont5 = num.count(5)
print(f'Foram digitados {tam} números.')
print(f'Os números digitados em ordem decrescente são: {sorted(num, reverse=True)}')
if cont5 > 0:
    print(f'{cores["verde"]}O número 5 está na lista{cores["limpa"]}')
else:
    print(f'{cores["vermelho"]}O número 5 não está na lista{cores["limpa"]}')
print('FIM')