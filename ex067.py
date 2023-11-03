cores = {'limpa': '\033[m',
         'azul': '\033[1;34m'}
print(f'{cores ["azul"]}-=' * 20)
print('TABUADA - BREAK')
print('-=' * 20, f'{cores ["limpa"]}')
while True:
    num = int(input('[Digite um número negativo para encerrar]\nDigite um número para ver sua tabuada: '))
    if num < 0:
        break
    for c in range(1, 11):
        print(f'{num:2} * {c:2} = {c * num:2}')
print('FIM')
