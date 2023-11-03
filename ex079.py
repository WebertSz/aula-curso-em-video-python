print('-=' * 20)
print('LISTA - VÁRIOS VALORES ORDEM CRESCENTE')
print('-=' * 20)
num = []
while True:
    n = int(input('Digite um número: '))
    if n not in num:
        num.append(n)
        print('Valor adicionado com sucesso!')
    else:
        print('Valor já existente. Não adicionado!')
    escolha = ' '
    while escolha not in 'SN':
        escolha = input('Deseja digitar outro número? [S/N]: ').strip().upper()
    if escolha == 'N':
        break
print(num)
print(f'Os números digitados em ordem crescente são {sorted(num)}')
print('FIM')
