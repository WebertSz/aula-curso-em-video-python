larg = float(input('Qual a largura da parede?'))
alt = float(input('Qual a altura da parede?'))
area: float = larg * alt
print('Será necessário {} litros de tinta para pintar a parede'.format(area / 2))
