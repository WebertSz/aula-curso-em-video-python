import datetime

print('-=' * 20)
print('DICIONÁRIO - CARTEIRA DE TRABALHO')
print('-=' * 20)
cadastro = dict()
cadastro["Nome"] = str(input('Digite o nome: ')).strip().upper()
nascimento = int(input('Digite o ano de nascimento: '))
cadastro["Idade"] = datetime.date.today().year - nascimento
valid = ' '
while valid not in 'SN':
    valid = str(input('Possui carteira de trabalho: [S/N]: ')).strip().upper()
if valid == 'S':
    cadastro["CTPS"] = int(input('Digite o número da carteira de trabalho: '))
    cadastro["Contratação"] = int(input('Digite o ano de contratação: '))
    cadastro["Salário"] = float(input('Digite o salário R$ '))
    cadastro["Aposentadoria"] = cadastro["Contratação"] + 35 - nascimento
else:
    cadastro["CTPS"] = 0
for i in cadastro:
    print(f'{i} tem o valor de {cadastro[i]}')
print('FIM')
