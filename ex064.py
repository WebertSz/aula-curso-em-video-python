cores = {'limpa': '\033[m',
         'azul': '\033[1;34m',
         'vermelho': '\033[1;31m'}
print('{}-='.format(cores['azul']) * 20)
print('SOMA - STOP 999')
print('-=' * 20, '{}'.format(cores['limpa']))
num = cont = soma = 0
while num != 999:
    num = int(input('PARA PARAR DIGITE 999\n'
                    'Digite um número: '))
    if num != 999:
        soma += num
        cont += 1
    else:
        print('Tem certeza que deseja sair?')
        valid = ''
        while valid != 'V':
            sair = input('Escolha [S/N]: ').strip().upper()[0]
            if sair == 'S':
                valid = 'V'
            elif sair == 'N':
                valid = 'V'
                num = 0
            else:
                print('{}Inválido!{}'.format(cores['vermelho'], cores['limpa']))
                valid = 'F'
print('Você digitou {} números e a soma desses números foi {}.'.format(cont, soma))
print('Fim')
