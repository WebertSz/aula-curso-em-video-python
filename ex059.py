cores = {'limpa': '\033[m',
         'azul': '\033[1;34m',
         'vermelho': '\033[1;31m'
         }
print('{}-='.format(cores['azul']) * 20)
print('OPERAÇÕES MATEMÁTICAS')
print('-=' * 20, '{}'.format(cores['limpa']))
menu = 4
valid = ''
while menu != 5:
    valid = 'F'
    while valid != 'V':
        if menu == 4:
            num1 = int(input('Digite o primeiro número: '))
            num2 = int(input('Digite o segundo número: '))
            menu = 0
        else:
            menu = int(input('''
            MENU
            [1]SOMAR
            [2]MULTIPLICAR
            [3]MAIOR
            [4]NOVOS NÚMEROS
            [5]SAIR
            Escolha sua opção: '''))
            if menu == 1:
                total = num1 + num2
                print('A soma entre {} e {} é {}'.format(num1, num2, total))
            elif menu == 2:
                total = num1 * num2
                print('A multiplicação entre {} e {} é {}'.format(num1, num2, total))
            elif menu == 3:
                if num1 > num2:
                    print('Entre {} e {} o maior número é o {}'.format(num1, num2, num1))
                elif num1 < num2:
                    print('Entre {} e {} o maior número é o {}'.format(num1, num2, num2))
                else:
                    print('Os dois números são iguais')
            elif menu == 5:
                print('Deseja realmente sair?')
                valid = ''
                while valid != 'V':
                    sair = input('Escolha [S/N]: ').strip().upper()[0]
                    if sair == 'S':
                        valid = 'V'
                    elif sair == 'N':
                        valid = 'V'
                        menu = 4
                    else:
                        print('{}Opção inválida!{}'.format(cores['vermelho'], cores['limpa']))
                        valid = 'F'
            else:
                if menu != 4:
                    print('{}Opção inválida!{}'.format(cores['vermelho'], cores['limpa']))
print('Programa encerrado!')
