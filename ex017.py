import math
oposto = float(input('Digite o cateto oposto do triângulo: '))
adjacente = float(input('Digite o cateto adjacente do triângulo: '))
print('O valor da hipotenusa é {:.3f}'.format(math.hypot(oposto, adjacente)))
