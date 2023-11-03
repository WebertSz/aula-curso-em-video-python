radar = int(input('Digite a velocidade do carro: '))
if radar > 80:
    multa: float = (radar - 80) * 7.00
    print('Sua velocidade foi {} km/h. Você foi multado em R$ {:.2f}!'.format(radar, multa))
else:
    print('Muito bem, você está dentro da velocidade permitida de 80km/h!')
print('Fim.')