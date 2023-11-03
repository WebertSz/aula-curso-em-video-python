cores = {'limpa': '\033[m',
         'azul': '\033[1;34m'}
print(f'{cores ["azul"]}-=' * 20)
print('SOMA NÚMERO - BREAK 999')
print('-=' * 20, f'{cores ["limpa"]}')
soma = cont = 0
while True:
    num = int(input('[Digite 999 para encerrar]\nDigite um número: '))
    if num == 999:
        break
    soma += num
    cont += 1
print(f'A soma dos {cont} valores foi {soma}')