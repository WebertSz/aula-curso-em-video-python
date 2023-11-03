print('-=' * 20)
print('LISTA DENTRO DE LISTA 86 e 87 - MATRIZ 86 - SOMA 87')
print('-=' * 20)
matriz = list()
dados = list()
somaCol = somaPar = 0
for linha in range(0, 3):
    for coluna in range(0, 3):
        dados.append(int(input(f'Digite o valor para [{linha},{coluna}]: ')))
    matriz.append(dados[:])
    dados.clear()
print(matriz)
for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[{matriz[linha][coluna]:^5}]', end='')
        if matriz[linha][coluna] % 2 == 0:
            somaPar += matriz[linha][coluna]
    print()
print(f'A soma dos valores pares é: {somaPar}')
for linha in range(0, 3):
    somaCol += matriz[linha][2]
print(f'A soma dos valores na terceira coluna é: {somaCol}')
print(f'O maior valor na segunda linha é: {max(matriz[1])}')
print('FIM')
