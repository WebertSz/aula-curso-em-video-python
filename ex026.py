frase = input('Digite uma frase: ').lower().strip()
print(' A letra "a" aparece {} vezes na frase.'.format(frase.count('a')))
print(' A primeira letra "a" aparece na posição {}'.format(frase.find('a')+1))
print('A última letra "a" aparece na posição {}'.format(frase.rfind('a')+1))
