import  datetime
cores = {'limpa': '\033[m',
         'vermelho': '\033[1;31m',
         'verde': '\033[1;32m',
         'amarelo': '\033[1;33m',
         'azul': '\033[1;34m',
         'roxo': '\033[1;35m',
         'cinza': '\033[1;37m'}
print('{}-='.format(cores['azul'])*20)
print('Categoria de Natação')
print('-='*20, '{}'.format(cores['limpa']))
nasc = int(input('Digite o ano de seu nascimento: '))
ano = datetime.date.today().year
idade = ano - nasc
if idade <= 9:
    print('{}Sua categoria é Mirim!{}'.format(cores['vermelho'], cores['limpa']))
elif idade <= 14:
    print('{}Sua categoria é Infantil{}'.format(cores['verde'], cores['limpa']))
elif idade <= 19:
    print('{}Sua categoria é Junior!{}'.format(cores['amarelo'], cores['limpa']))
elif idade <= 25:
    print('{}Sua categoria é Senior!{}'.format(cores['roxo'], cores['limpa']))
else:
    print('{}Sua categoria é Master{}'.format(cores['cinza'], cores['limpa']))
print('FIM')
