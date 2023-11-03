cores = {'limpa': '\033[m',
         'azul': '\033[1;34m'}
print('{}-='.format(cores['azul']) * 20)
print('Analise de Pessoas')
print('-=' * 20, '{}'.format(cores['limpa']))
idgrupo = 0
maior = 0
nomemaior = ''
qtde = 0
for c in range(0,4):
    nome = input('Digite seu nome: ').strip().upper()
    idade = int(input('Digite sua idade: '))
    print('''Escolha seu sexo:
    M - Masculino
    F - Feminino
    ''')
    sexo = input('Escolha seu sexo: ').strip().upper()
    idgrupo += idade
    if sexo == 'M':
        if idade > maior:
            maior = idade
            nomemaior = nome
    elif sexo == 'F':
        if idade < 20:
            qtde += 1
    else:
        print('Sexo inválido. Digite novamente!')
print('A média de idade do grupo de pessoas é {:.1f}!'.format(idgrupo / 4))
print('{} tem {} anos e é o homem mais velho do grupo!'.format(nomemaior, maior))
print('Tem {} mulher(es) menor(es) de 20 ano(s) nesse grupo de pessoas!'.format(qtde))
print('Fim')
