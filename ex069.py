cores = {'limpa': '\033[m',
         'azul': '\033[1;34m',
         'vermelho': '\033[1;31m'}
print(f'{cores["azul"]}-=' * 20)
print('ANÁLISE DE DADOS - BREAK')
print('-=' * 20, f'{cores["limpa"]}')
contid = conth = contm20 = 0
while True:
    idade = int(input('Digite a idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = input('Escolha: [M/F]').strip().upper()
    if idade > 18:
        contid += 1
    if sexo == 'M':
        conth += 1
    if sexo == 'F' and idade < 20:
        contm20 += 1
    escolha = ' '
    while escolha not in 'SN':
        escolha = input('Deseja fazer outro cadastro. Escolha [S/N]: ').strip().upper()
    if escolha == 'N':
        break
print(f'Total de pessoa maiores de 18 anos: {contid}.')
print(f'Total de homens cadastrados: {conth}.')
print(f'Total de mulheres com menos de 20 anos: {contm20}.')
print('FIM')
