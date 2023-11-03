cores = {'limpa': '\033[m',
         'azul': '\033[1;34m',
         'vermelho': '\033[1;31m'}
print(f'{cores["azul"]}-=' * 20)
print('CAIXA ELETRÔNICO - BREAK')
print('-=' * 20, f'{cores["limpa"]}')
totced = 0
saque = int(input('Digite o valor do saque: R$ '))
ced = 50
while True:
    if saque > 0:
        totced = saque // ced
        saque -= ced * totced
        print(f'Total de {totced} cédulas de R$ {ced:.2f}.')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
    else:
        break
print('FIM')
