print('-=' * 20)
print('LISTA DENTRO DE LISTA - PAR e ÍMPAR')
print('-=' * 20)
valores = [[], []]
num = 0
for i in range(1, 8):
    num = int(input(f'Digite o {i}º número: '))
    if num % 2 == 0:
        valores[0].append(num)
    else:
        valores[1].append(num)
print(valores)
print(f'Os valores pares digitados são {sorted(valores[0])}.')
print(f'Os valores ímpares digitados são {sorted(valores[1])}.')
print('FIM')
