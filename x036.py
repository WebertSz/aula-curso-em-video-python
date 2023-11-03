cores = {'limpa': '\033[m', 'verde': '\033[1;32m', 'vermelho': '\033[1;31m', 'azul': '\033[1;34m'}
print('{}-='.format(cores['azul'])*20)
print('Análise de Empréstimo Bancário')
print('-='*20)
casa = float(input('{}Digite o valor da casa: '.format(cores['limpa'])))
salario = float(input('Digite o valor do seu salário: '))
ano = int(input('Digite quantos anos vai pagar: '))
parcela = casa / (ano * 12)
if parcela < salario / 100 * 30:
    print('{}Empréstimo concedido. O valor da parcela será de R$ {:.2f}.{}'.format(cores['verde'], parcela, cores['limpa']))
else:
    print('{}Empréstimo negado, seu salário é muito baixo.{}'.format(cores['vermelho'], cores['limpa']))
