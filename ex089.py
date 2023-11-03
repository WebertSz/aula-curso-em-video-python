print('-=' * 20)
print('LISTA DENTRO DE LISTA - NOTAS ALUNOS')
print('-=' * 20)
alunos = list()
while True:
    nome = str(input('Digite o nome do aluno: ')).strip().upper()
    nota1 = float(input('Digite a 1ª nota do aluno: '))
    nota2 = float(input(f'Digite a 2ª nota do aluno: '))
    media = (nota1 + nota2) / 2
    alunos.append([nome, [nota1, nota2], media])
    escolha = ' '
    while escolha not in 'SN':
        escolha = input('Deseja continuar cadastrando? [S/N]: ').strip().upper()
    if escolha == 'N':
        break
print(alunos)
print(f'{"Nº.":<4}{"NOME":<10} {"MEDIA":>8}')
print('-' * 26)
for pos, pessoa in enumerate(alunos):
    print(f'{pos:<4}{pessoa[0]:<10}{pessoa[2]:>8.1f}')
while True:
    print('-' * 30)
    notaAluno = int(input('Mostra a nota de qual aluno? '))
    print(f'Nota do {alunos[notaAluno][0]} são {alunos[notaAluno][1]}')
    escolha = ' '
    while escolha not in 'SN':
        escolha = input('Deseja mostrar nota de outro aluno? [S/N]: ').strip().upper()
    if escolha == 'N':
        break
print('FIM')
