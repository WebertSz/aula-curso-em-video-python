cores = {'limpa': '\033[m',
         'azul': '\033[1;34m',
         'vermelho': '\033[1;31m'
         }
print('{}-='.format(cores['azul']) * 20)
print('Escolha o Sexo')
print('-=' * 20, '{}'.format(cores['limpa']))
sexo = ' '
while sexo not in 'MF':
    sexo = input('Digite o sexo [M/F]: ').strip().upper()[0]
    if sexo != 'M/F':
        print('{}Inválido!{}'.format(cores['vermelho'], cores['limpa']))
print('Seu sexo é {}!'.format(sexo))
print('Fim')
