print('-=' * 20)
print('DICIONÁRIO - MÉDIA DO ALUNO')
print('-=' * 20)
aluno = dict()
aluno['Nome'] = str(input('Digite o nome do(a) aluno(a): ')).strip().upper()
aluno['Média'] = float(input(f'Digite a média do(a) {aluno["Nome"]}: '))
if aluno['Média'] >= 6:
    aluno['Situação'] = 'Aprovado(a)'
else:
    aluno['Situação'] = 'Reprovado(a)'
print(f'{aluno["Nome"]} teve a média {aluno["Média"]} e foi {aluno["Situação"]}')
print('Fim')
