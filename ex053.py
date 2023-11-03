cores = {'limpa': '\033[m',
         'azul': '\033[1;34m'}
print('{}-='.format(cores['azul']) * 20)
print('Palíndromo')
print('-=' * 20, '{}'.format(cores['limpa']))
frase = input('Digite uma frase: ').strip().upper().split()
frasejunta = ''.join(frase)
palindromo = ''
for c in range(len(frasejunta)-1, -1, -1):
    palindromo += frasejunta[c]
if frasejunta == palindromo:
    print('A frase "{}", é um Palíndromo!'.format(palindromo))
else:
    print('A frase não é Palíndromo!')
print('Fim')