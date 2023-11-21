from time import sleep


def titulo(txt):
    print('-=' * 20)
    print(txt)
    print('-=' * 20)


def verificarMaior(* valores):
    maior = 0
    print('-=' * 20)
    print('Analisando os valores...')
    for numero in valores:
        sleep(1)
        print(f'{numero}', end=' ')
        if numero > maior:
            maior = numero
    print(f'Foram analisados {len(valores)} valores')
    print(f'O maior valor é {maior}')
    print('-=' * 20)


titulo("FUNÇÃO - ANALISANDO VALORES")
verificarMaior(2, 9, 4, 5, 7, 1)
verificarMaior(4, 7, 0)
verificarMaior(1, 2)
verificarMaior(6)
verificarMaior()
