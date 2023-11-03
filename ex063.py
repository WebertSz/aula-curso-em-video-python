cores = {'limpa': '\033[m',
         'azul': '\033[1;34m', }
print('{}-='.format(cores['azul']) * 20)
print('SEQUÊNCIA FIBONACCI')
print('-=' * 20, '{}'.format(cores['limpa']))
num = int(input('Digite um número para ver a sequência de Fibonacci: '))
cont = 0
fib = 0
pen = 0
ult = 0
while cont != num:
    if cont % 2 == 0:
        if ult == 0:
            pen = 0
        ult = fib
    else:
        if pen == 0:
            fib = 1
        pen = fib
    fib = pen + ult
    print('{} '.format(fib), end='')
    cont += 1
print('\nFim')