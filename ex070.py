cores = {'limpa': '\033[m',
         'azul': '\033[1;34m',
         'vermelho': '\033[1;31m'}
print(f'{cores["azul"]}-=' * 20)
print('PRODUTOS - BREAK')
print('-=' * 20, f'{cores["limpa"]}')
soma = menor = cont = 0
barato = ''
while True:
    produto = str(input('Digite o produto: ')).strip().upper()
    preço = int(input('Digite o preço do produto: R$ '))
    soma += preço
    if preço > 1000:
        cont += 1
    if menor == 0 or preço < menor:
        menor = preço
        barato = produto
    escolha = ' '
    while escolha not in 'SN':
        escolha = input('Deseja cadastrar outro produto? Escolha [S/N]: ').strip().upper()
    if escolha == 'N':
        break
print(f'O total da compra é R$ {soma:.2f}')
print(f'{cont} produtos custam mais de R$ 1000.00')
print(f'O produto mais barato foi {barato} e custou R$ {menor:.2f}')
print('FIM')
