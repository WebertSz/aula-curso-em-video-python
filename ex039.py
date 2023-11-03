import datetime
cores = {'limpa': '\033[m',
         'vermelho': '\033[1;31m',
         'verde': '\033[1;32m',
         'amarelo': '\033[1;33m',
         'azul': '\033[1;34m'}
print('{}-='.format(cores['azul'])*20)
print('Alistamento Militar')
print('-='*20, '{}'.format(cores['limpa']))
nasc = int(input('Digite o ano de seu nascimento: '))
ano = datetime.date.today().year
tempo = ano - nasc
if tempo == 18:
    print('{}Este ano você deve se alistar ao Serviço Militar!{}'.format(cores['verde'], cores['limpa']))
elif tempo < 18:
    falta = 18 - tempo
    print('{}Falta {} ano(s) para se alistar ao Serviço Militar!{}'.format(cores['amarelo'], falta, cores['limpa']))
else:
    passou = tempo - 18
    print('{}Já passou {} ano(s) que você deveria ter se alistado ao Serviço Militar!{}'
          .format(cores['vermelho'], passou, cores['limpa']))
print('FIM.')
