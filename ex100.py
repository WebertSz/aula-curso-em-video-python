from random import randint
from time import sleep


def titulo(txt):
    print('-=' * 20)
    print(txt)
    print('-=' * 20)


def sortearNumeros():
    listaNumeros = []
    print('Sorteando 5 números...')
    for sorteio in range(0, 5):
        listaNumeros.append(randint(1, 10))
    for i in listaNumeros:
        sleep(1)
        print(f'{i}', end=' ')
    print()
    return listaNumeros


def somarNumerosPares(lista):
    soma = 0
    for numero in lista:
        if numero % 2 == 0:
            soma += numero
    print(f'A soma de todos os valores pares da lista {lista} é {soma}')


titulo('FUNÇÃO - SOMA VALORES PARES')
somarNumerosPares(sortearNumeros())
