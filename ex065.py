cores = {'limpa': '\033[m',
         'azul': '\033[1;34m',
         'vermelho': '\033[1;31m'}
print('{}-='.format(cores['azul']) * 20)
print('MÉDIA NÚMEROS')
print('-=' * 20, '{}'.format(cores['limpa']))
valid = ''
soma = cont = maior = menor = 0
while valid != 'N':
    num = int(input('Digite um número: '))
    soma += num
    if cont == 0:
        maior = num
        menor = num
    if num > maior:
        maior = num
    if num < menor:
        menor = num
    cont += 1
    valid = ' '
    while valid not in 'SN':
        print('Deseja digitar outro número?')
        valid = input('Escolha [S/N]: ').strip().upper()[0]
        if valid not in 'SN':
            print('{}Inválido!{}'.format(cores['vermelho'], cores['limpa']))
print('A média dos números digitados foi {:.2f}, o maior número foi {}, e o menor foi {}'
      .format(soma / cont, maior, menor))
print('Fim')