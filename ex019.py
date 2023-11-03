import random
aluno1 = input('Escreva o nome do aluno: ')
aluno2 = input('Escreva o nome do segundo aluno: ')
aluno3 = input('Escreva o nome do terceiro aluno: ')
aluno4 = input('Escreva o nome do quarto aluno: ')
lista = [aluno1, aluno2, aluno3, aluno4]
sorteio = random.choice(lista)
print('O aluno sorteado para limpar o quadro é {}'.format(sorteio))
