print('-=' * 20)
print('TUPLA - LISTAGEM DE PREÇOS')
print('-=' * 20)
listagem = ('Pão', 1.00, 'Leite', 4.50, 'Bolo', 12, 'Salgadinho', 105)
for pos, c in enumerate(listagem):
    if pos % 2 == 0:
        print(f'{c:.<20}', end=' ')
    else:
        print(f'R$ {c:>6.2f}', end='\n')
print('FIM')
