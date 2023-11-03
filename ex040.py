cores = {'limpa': '\033[m',
         'vermelho': '\033[1;31m',
         'verde': '\033[1;32m',
         'amarelo': '\033[1;33m',
         'azul': '\033[1;34m'}
print('{}-='.format(cores['azul'])*20)
print('Média do Aluno')
print('-='*20, '{}'.format(cores['limpa']))
nota1 = float(input('Digite a primeira nota do aluno: '))
nota2 = float(input('Digite a segunda nota do aluno: '))
media = (nota1 + nota2) / 2
if media >= 7.0:
    print('{}A média é {}, o aluno foi aprovado!{}'.format(cores['verde'], media, cores['limpa']))
elif media < 5.0:
    print('{}A média do aluno é {}, o aluno foi reprovado!{}'.format(cores['vermelho'], media, cores['limpa']))
else:
    print('{}A média do aluno é {}, o aluno está em recuperação!{}'.format(cores['amarelo'], media, cores['limpa']))
print('FIM')
