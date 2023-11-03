print('-=' * 20)
print('TUPLA - NÚMERO EM EXTENSO')
print('-=' * 20)
num = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze',
       'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    n = int(input('Digite um número de 0 à 20: '))
    if 0 <= n <= 20:
        print(f'Você digitou o número {num[n]}')
        break
print('FIM')