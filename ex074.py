from random import randint

print('-=' * 20)
print('TUPLA - NÚMEROS ALEATÓRIOS')
print('-=' * 20)
num = (randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100),
       randint(0, 100),)
print(num)
print(f'O menor número é o {min(num)}.')
print(f'O maior número é o {max(num)}.')
print('FIM')
