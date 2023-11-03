cores = {'limpa': '\033[m',
         'verde': '\033[1;32m',
         'vermelho': '\033[1;31m',
         'amarelo': '\033[1;33m',
         'azul': '\033[1;34m'}
print('{}-='.format(cores['azul']) * 20)
print('Conversão Binário, Décima, Hexadécimal')
print('-=' * 20)
num = int(input('{}Digite o número: '.format(cores['limpa'])))
conversor = int(input('Digite 1 - Para Binário \n'
                      'Digite 2 - Para Octal \n'
                      'Digite 3 - Para Hexadecimal: ').strip().upper())
if conversor == 1:
    binario = format(num, 'b')
    print('{}O número {} convertido em Binário é {}.{}'.format(cores['verde'], num, binario, cores['limpa']))
elif conversor == 2:
    octal = format(num, 'o')
    print('{}O número {} convertido em Octal é {}.{}'.format(cores['vermelho'], num, octal, cores['limpa']))
else:
    hexa = format(num, 'x')
    print('{}O número {} convertido em hexadecimal é {}.{}'.format(cores['amarelo'], num, hexa, cores['limpa']))
