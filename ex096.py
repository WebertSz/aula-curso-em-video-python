def titulo(txt):
    print('-=' * 20)
    print(txt)
    print('-=' * 20)


def area(l, c):
    print(f'A area de um terreno {l}x{c} é de {largura * comprimento}m².')


titulo('FUNÇÃO - CALCULO DE AREA DE UM RETÂNGULO')
largura = float(input('Digite a largura (m): '))
comprimento = float(input('Digite o comprimento (m): '))
area(largura, comprimento)
