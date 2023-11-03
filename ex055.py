cores = {'limpa': '\033[m',
         'azul': '\033[1;34m'}
print('{}-='.format(cores['azul']) * 20)
print('Maior e Menor Peso')
print('-=' * 20, '{}'.format(cores['limpa']))
maior = 0
menor = 0
for c in range(1, 6):
    peso = float(input('Digite o seu peso: '))
    if c == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O maior peso é {:.2f} KG e o menor peso é {:.2f} KG!'.format(maior, menor))
print('Fim')

