print('-=' * 20)
print('DICIONÁRIO - CADASTRO DE VÁRIOS JOGADORES DE FUTEBOL')
print('-=' * 20)
jogador = dict()
cadastro = list()
gols = list()
while True:
    gols.clear()
    jogador['Nome'] = str(input('Digite o nome do jogador: ')).upper().strip()
    totalDePartidas = int(input(f'Digita quantas partidas {jogador["Nome"]} jogou: '))
    for partida in range(totalDePartidas):
        gols.append(int(input(f'Digite quantos gols na partida {partida + 1}: ')))
    jogador['Gols'] = gols[:]
    jogador['Total de Gols'] = sum(gols)
    cadastro.append(jogador.copy())
    print(cadastro)
    escolha = ' '
    while escolha not in 'SN':
        escolha = input('Deseja continuar cadastrando? [S/N]: ').strip().upper()
    if escolha == 'N':
        break
print('-=' * 30)
print('cod', end=' ')
for i in jogador.keys():
    print(f'{i:<15}', end=' ')
print()
print('-' * 50)
for pos, values in enumerate(cadastro):
    print(f'{pos + 1:>3}|', end=' ')
    for item in values.values():
        print(f'{str(item):<15}', end=' ')
    print()
print('-' * 50)
while True:
    print('Mostrar dados de qual jogador:')
    for pos, menu in enumerate(cadastro):
        print(f'{pos + 1} | {menu["Nome"]}')
    busca = int(input('Mostrar dados de qual jogador: '))
    if busca > len(cadastro) or busca <= 0:
        print(f'Não existe jogador com o código {busca}!')
    else:
        print('-- RESULTADO DA BUSCA --')
        print(f'{cadastro[busca - 1]["Nome"]}')
        for pos, golsPartida in enumerate(cadastro[busca - 1]["Gols"]):
            print(f'No jogo {pos + 1} fez {golsPartida} gols')
    escolha = ' '
    while escolha not in 'SN':
        escolha = input('Deseja mostra dados de outro jogador? [S/N]: ').strip().upper()
    if escolha == 'N':
        break
print("Fim")
