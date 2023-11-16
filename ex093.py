print('-=' * 20)
print('DICIONÁRIO - CADASTRO JOGADOR DE FUTEBOL')
print('-=' * 20)
jogador = dict()
gols = list()
jogador['Nome'] = str(input('Digite o nome do jogador: ')).upper().strip()
totalDePartidas = int(input(f'Digita quantas partidas {jogador["Nome"]} jogou: '))
for partida in range(totalDePartidas):
    gols.append(int(input(f'Digite quantos gols na partida {partida + 1}: ')))
jogador['Gols'] = gols
jogador['Total de Gols'] = sum(gols)
print(jogador)
for keys, values in jogador.items():
    print(f'O campo {keys} tem o valor de {values}.')
print(f'O jogador {jogador["Nome"]} jogou {totalDePartidas} partidas.')
for partida in range(totalDePartidas):
    if gols[partida] == 0:
        print(f'{"":<5} => Na partida {partida + 1}, não fez gol')
    else:
        print(f'{"":<5} => Na partida {partida + 1}, fez {gols[partida]} gol(s)')
print(f'No total foram {jogador["Total de Gols"]} gols.')
print("Fim")
