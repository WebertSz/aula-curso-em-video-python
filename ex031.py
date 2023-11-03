distancia = int(input('Digite a distância da viagem: '))
if distancia <= 200:
    passagem: float = distancia * 0.50
    print('O valor da passagem é de R$ {:.2f}.'.format(passagem))
else:
    passagem: float = distancia * 0.45
    print('O valor da passagem é de R$ {:.2f}.'.format(passagem))
print('Obrigado por viajar conosco. Boa viagem!')
