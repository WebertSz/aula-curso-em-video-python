n = int(input('Digite um número para ver a sua tabuada:'))
i = 1
while i < 10:
    print('{} * {} = {:2}'.format(n, i, (n * i)))
    i += 1
