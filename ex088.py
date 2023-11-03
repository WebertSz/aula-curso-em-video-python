from random import randint
from time import sleep
print('-=' * 20)
print('LISTA DENTRO DE LISTA - SORTEADOR MEGA SENA')
print('-=' * 20)
palpites = list()
jogos = list()
totjogos = int(input('Digite quantos jogos deseja jogar: '))
print('-=' * 5, f'SORTEANDO {totjogos} JOGOS', '-=' * 5)
for j in range(0, totjogos):
    for n in range(0, 6):
        palpites.append(randint(1, 60))
        for repetido in palpites:
            cont = palpites.count(repetido)
            if cont > 1:
                palpites.pop()
                palpites.append(randint(1, 60))
    jogos.append(palpites[:])
    palpites.clear()
    print(f'Jogo {j + 1}: {sorted(jogos[j])}')
    sleep(1)
print('-=' * 6, 'BOA SORTE!', '-=' * 7)
print('FIM')
