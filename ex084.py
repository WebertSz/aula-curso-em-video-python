print('-=' * 20)
print('LISTA DENTRO DE LISTA - MAIOR E MENOR PESO')
print('-=' * 20)
dados = list()
cadastro = list()
qtde = maior = menor = 0
while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))
    cadastro.append(dados[:])
    if maior == 0 and menor == 0:
        maior = menor = dados[1]
    else:
        if dados[1] > maior:
            if dados[1] > maior:
                maior = dados[1]
        if dados[1] <= menor:
            if dados[1] < menor:
                menor = dados[1]
    dados.clear()
    qtde += 1
    escolha = ' '
    while escolha not in 'SN':
        escolha = input('Deseja continuar cadastrando? [S/N]: ').strip().upper()
    if escolha == 'N':
        break
print(f'Foram cadastradas {qtde} pessoas.')
print(f'O maior peso cadastrado foi de {maior}Kg:', end='')
for pessoas in cadastro:
    if pessoas[1] == maior:
        print(f' {pessoas[0]}', end='')
print(f'\nO menor peso cadastrado foi de {maior}Kg. Peso de', end='')
for pessoas in cadastro:
    if pessoas[1] == menor:
        print(f' {pessoas[0]}', end='')
print('\nFIM')
