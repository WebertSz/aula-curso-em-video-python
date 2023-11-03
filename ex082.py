print('-=' * 20)
print('LISTA - PAR/ÍMPAR')
print('-=' * 20)
num = []
par = []
impar = []
while True:
    num.append(int(input('Digite um número: ')))
    escolha = ' '
    while escolha not in 'SN':
        escolha = input('Deseja digitar outro número: [S/N]: ').strip().upper()
    if escolha == 'N':
        break
for n in num:
    if n % 2 == 0:
        par.append(n)
    else:
        impar.append(n)
print(f'A lista completa dos valores digitados é: {num}')
print(f'Os valores pares digitados são: {par}')
print(f'Os valores ímpares digitados são: {impar}')
print('FIM')