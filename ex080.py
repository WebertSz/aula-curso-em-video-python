print('-=' * 20)
print('LISTA - VÁRIOS VALORES ORDENADOS')
print('-=' * 20)
lista = []
num = 0
for n in range(0, 5):
    num = int(input('Digite um número: '))
    if n == 0 or n > lista[- 1]:
        lista.append(num)
        print(f'O número {num} foi adicionado no final da lista')
    for pos, t in enumerate(lista):
        if num < t:
            lista.insert(pos, num)
            print(f'O número {num} foi adicionado na posição {pos}')
            num = t
        elif num > t:
            tam = len(lista)-1
            if num > t and pos == tam:
                lista.append(num)
                print(f'O número {num} foi adicionado no final da lista')
        else:
            break
print(f'Os números em ordem são {lista}')
print('FIM')
