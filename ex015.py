dias = int(input('Por quantos dias o carro foi alugado?'))
km = float(input('Quantos Km percorridos?'))
print('O valor a pagar é R$ {:.2f}'.format((60 * dias) + (0.15 * km)))
