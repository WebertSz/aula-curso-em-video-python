print('-=' * 20)
print('DICIONÁRIO - MÉDIA DO ALUNO')
print('-=' * 20)
aluno = dict()
aluno['Nome'] = str(input('Digite o nome do aluno: ')).strip().upper()
aluno['Média'] = float(input('Digite a média do aluno: '))
if aluno['Média'] >= 6:
    aluno['Situação'] = 'Aprovado(a)'
else:
    aluno['Situação'] = 'Reprovado(a)'
print(f'{aluno["Nome"]} teve a média {aluno["Média"]} e foi {aluno["Situação"]}')
print('Fim')
