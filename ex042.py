cores = {'limpa': '\033[m', 'azul': '\033[1;34m', 'verde': '\033[1;32m', 'vermelho': '\033[1;31m'}
print('{}-='.format(cores['azul'])*20)
print('Analisador de triângulo')
print('-='*20, '{}'.format(cores['limpa']))
reta1 = float(input('Digite o tamanho da primeira reta: '))
reta2 = float(input('Digite o tamanho da segunda reta: '))
reta3 = float(input('Digite o tamanho da terceira reta: '))
if reta1 + reta2 > reta3 and reta1 + reta3 > reta2 and reta2 + reta3 > reta1:
    if reta1 == reta2 == reta3:
        print('{}As retas formam um triângulo Equilátero!{}'.format(cores['verde'], cores['limpa']))
    elif reta1 != reta2 != reta3 != reta1:
        print('{}As retas formam um triângulo Escaleno!{}'.format(cores['verde'], cores['limpa']))
    else:
        print('{}As retas formam um triângulo Isósceles!{}'.format(cores['verde'], cores['limpa']))
else:
    print('{}As retas não formam um triângulo!{}'.format(cores['vermelho'], cores['limpa']))
print('Fim.')
