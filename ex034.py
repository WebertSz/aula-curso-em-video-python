salario = float(input('Digite o salário do funcionário: R$ '))
if salario > 1250.00:
    aumento = salario + (salario * 10 / 100)
    print('O novo salário do funcionário é de R$ {:.2f}'.format(aumento))
else:
    aumento = salario + (salario * 15 / 100)
    print('O novo salário do funcionário é de R$ {:.2f}'.format(aumento))
print('Fim')
