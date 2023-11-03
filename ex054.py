from  datetime import date

cores = {'limpa': '\033[m',
         'azul': '\033[1;34m'}
print('{}-='.format(cores['azul']) * 20)
print('Maior e Menor Idade')
print('-=' * 20, '{}'.format(cores['limpa']))
data = date.today().year
maior = 0
menor = 0
for c in range(0, 7):
    nasc = int(input('Digite a data de nascimento: '))
    cont = data - nasc
    if cont > 18:
        maior += 1
    else:
        menor += 1
print(f'{maior} pessoas são maiores de idade e {menor} são menores de idade!')
print('Fim')
