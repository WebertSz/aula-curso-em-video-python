from random import randint
from time import sleep
print('-=' * 20)
print('DICIONÁRIO - JOGO DO DADO')
print('-=' * 20)
ranking = 0
dado = {'Jogador 1': randint(1, 6),
        'Jogador 2': randint(1, 6),
        'Jogador 3': randint(1, 6),
        'Jogador 4': randint(1, 6)}
print('Valores Sorteados:')

for sorteio in dado:
    sleep(1)
    print(f'O Jogador {sorteio} tirou {dado[sorteio]}')
print('Ranking dos Jogadores:')
for ordem in sorted(dado, key = dado.get, reverse=True):
    ranking += 1
    sleep(1)
    print(f'O {ranking}º lugar foi o {ordem} com {dado[ordem]}')
print('FIM')
