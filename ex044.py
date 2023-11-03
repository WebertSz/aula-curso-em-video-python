cores = {'limpa': '\033[m',
         'vermelho': '\033[1;31m',
         'verde': '\033[1;32m',
         'amarelo': '\033[1;33m',
         'azul': '\033[1;34m',
         'roxo': '\033[1;35m'}
print('{}-='.format(cores['azul']) * 20)
print('Condição de Pagamento')
print('-=' * 20, '{}'.format(cores['limpa']))
valor = float(input('Digite o preço do produto: '))
print('''Formas de pagamento:
1 - Dinheiro/Cheque à vista 10% de desconto
2 - Cartão à vista 5% de desconto
3 - 2x no cartão sem desconto
4 - 3x ou mais no cartão 20% de juros
''')
pag = int(input('Digite a forma de pagamento: '))
if pag == 1:
    result = valor - (valor / 100 * 10)
    print('{}O valor a pagar é R$ {:.2f}.{}'.format(cores['verde'], result, cores['limpa']))
elif pag == 2:
    result = valor - (valor / 100 * 5)
    print('{}O valor à pagar é R$ {:.2f}.{}'.format(cores['roxo'], result, cores['limpa']))
elif pag == 3:
    valorparc = valor / 2
    print('{}O valor à pagar é R$ {:.2f}. Esse valor foi dividido em 2 parcelas de R$ {:.2f}.{}'
          .format(cores['amarelo'], valor, valorparc, cores['limpa']))
elif pag == 4:
    result = valor + (valor / 100 * 20)
    parcelas = int(input('Digite quantas parcelas: '))
    valorparc = result / parcelas
    print('{}O valor a pagar é R$ {:.2f}. Esse valor foi dividido em {} parcelas de R$ {:.2f}.{}'
          .format(cores['vermelho'], result, parcelas, valorparc, cores['limpa']))
else:
    print('{}Inválido. Digite a forma de pagamento novamente.{}'.format(cores['vermelho'], cores['limpa']))
print('FIM')
