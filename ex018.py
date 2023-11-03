import math
angulo = float(input('Digite o ângulo: '))
print('O ângulo é {}, o seu seno é {:.2f}, o cosseno é {:.2f} e a tangente é {:.2f}'
      .format(angulo, math.sin((math.radians(angulo))), math.cos(math.radians(angulo)),
              math.tan(math.radians(angulo))))
