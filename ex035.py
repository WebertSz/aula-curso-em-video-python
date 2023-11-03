cores = {'limpa': '\033[m', 'azul': '\033[1;34m', 'verde': '\033[1;32m', 'vermelho': '\033[1;31m'}
print('{}-='.format(cores['azul'])*20)
print('Analisador de triângulo')
print('-='*20)
reta1 = float(input('{}Digite o tamanho da primeira reta: '.format(cores['limpa'])))
reta2 = float(input('Digite o tamanho da segunda reta: '))
reta3 = float(input('Digite o tamanho da terceira reta: '))
if reta1 + reta2 > reta3 and reta1 + reta3 > reta2 and reta2 + reta3 > reta1:
    print('{}As retas formam um triângulo!{}'.format(cores['verde'], cores['limpa']))
else:
    print('{}As retas não formam um triângulo!{}'.format(cores['vermelho'], cores['limpa']))
print('Fim.')
