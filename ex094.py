print('-=' * 20)
print('DICIONÁRIO - CADASTRO DE PESSOAS')
print('-=' * 20)
pessoas = dict()
cadastro = list()
soma = 0
while True:
    pessoas['Nome'] = str(input('Digite o nome: ')).strip().upper()
    pessoas['Idade'] = int(input('Digite a idade: '))
    soma += pessoas['Idade']
    while True:
        pessoas['Sexo'] = (str(input('Digite o sexo [M/F]: '))).strip().upper()
        if pessoas['Sexo'] in 'MF':
            break
    cadastro.append(pessoas.copy())
    escolha = ' '
    while escolha not in 'SN':
        escolha = input('Deseja continuar cadastrando? [S/N]: ').strip().upper()
    if escolha == 'N':
        break
print(cadastro)
print(f'Foram cadastradas {len(cadastro)} pessoas.')
print(f'A média de idade é: {soma/len(cadastro)}')
print('As mulheres cadastradas são: ')
for mulher in cadastro:
    if mulher['Sexo'] == 'F':
        print(f'{mulher["Nome"]};', end=' ')
print('\nAs pessoas que estão acima da média de idade são: ')
for idadeMedia in cadastro:
    if idadeMedia['Idade'] > soma/len(cadastro):
        for keys, values in idadeMedia.items():
            print(f'{keys} = {values};', end=' ')
        print()
print('Fim')
