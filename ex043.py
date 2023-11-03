cores = {'limpa': '\033[m',
         'vermelho': '\033[1;31m',
         'verde': '\033[1;32m',
         'amarelo': '\033[1;33m',
         'azul': '\033[1;34m',
         'roxo': '\033[1;35m',
         'cinza': '\033[1;37m'}
print('{}-='.format(cores['azul'])*20)
print('Calculo de Massa Corporal')
print('-='*20, '{}'.format(cores['limpa']))
peso = float(input('Digite o seu peso: '))
altura = float(input('Digite sua altura: '))
imc: float = peso / (altura**2)
if imc < 18.5:
    print('{}Abaixo do peso.{}'.format(cores['vermelho'], cores['limpa']))
elif 18.5 <= imc < 25:
    print('{}Peso ideal.{}'.format(cores['verde'], cores['limpa']))
elif 25 <= imc < 30:
    print('{}Sobrepeso.{}'.format(cores['amarelo'], cores['limpa']))
elif 30 <= imc < 40:
    print('{}Obesidade.{}'.format(cores['roxo'], cores['limpa']))
else:
    print('{}Obesidade mórbida.{}'.format(cores['cinza'], cores['limpa']))
print('FIM')
