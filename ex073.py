print('-=' * 20)
print('TUPLA - TABELA BRASILEIRÃO')
print('-=' * 20)
tabela = ('Bota Fogo', 'Bragantino', 'Grêmio', 'Palmeiras', 'Flamengo', 'Fortaleza', 'Fluminense', 'Atlético-PR',
          'Atlético-MG', 'São Paulo', 'Cuiabá', 'Internacional', 'Corinthians', 'Santos', 'Cruzeiro', 'Bahia',
          'Vasco', 'Goiás', 'Coritiba', 'América')
print(f'Os cinco primeiro colocados na tabela são: ', end='')
for c in tabela[:5]:
    print(f'{c} ', end='')
print(f'\nOs quatro últimos colocados na tabela são: ', end='')
for c in tabela[16:]:
    print(f'{c} ', end='')
print(f'\nOs clubes do campeonato brasileiro em ordem alfabética são: {sorted(tabela)}.')
posição = tabela.index('Cruzeiro')
print(f'O Cruzeiro está na {posição + 1}ª posição.')
