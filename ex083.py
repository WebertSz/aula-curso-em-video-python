cores = {'limpa': '\033[m',
         'vermelho': '\033[1;31m',
         'verde': '\033[1;32m'}
print('-=' * 20)
print('LISTA - VERIFICAR SE EXPRESSÃO É VERDADEIRA')
print('-=' * 20)
exp = []
p1 = p2 = False
exp.append(str(input('Digite uma expressão: ')))
for p in exp:
    for parenteses in p:
        if parenteses in '(' and p1 == False and p2 == False:
            p1 = True
            for parenteses in p:
                if parenteses in ')' and p2 == False:
                    p2 = True
                else:
                    p2 = False
        elif parenteses in '(' and p1 == True and p2 == False:
            for parenteses in p:
                if parenteses in ')' and p2 == False:
                    p2 = True
                else:
                    p2 = False
        elif parenteses in '(' and p1 == True and p2 == True:
            p2 = False
            for parenteses in p:
                if parenteses in ')' and p1 == True and p2 == False:
                    p2 = True
                else:
                    p2 = False
        elif parenteses in ')' and p1 == False and p2 == False:
            p2 = True
            for parenteses in p:
                if parenteses in '(' and p1 == False:
                    p1 = True
                else:
                    p1 = False
        elif parenteses in ')' and p2 == True and p1 == False:
            for parenteses in p:
                if parenteses in '(' and p1 == False:
                    p1 = True
                else:
                    p1 = False
        elif parenteses in ')' and p2 == True and p1 == True:
            p2 = False
if p1 == True and p2 == True:
    print(f'{cores["verde"]} Essa expressão é válida!{cores["limpa"]}')
else:
    print(f'{cores["vermelho"]}Essa expressão é inválida!{cores["limpa"]}')
print('FIM')
