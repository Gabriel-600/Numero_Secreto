a = int(input('Informe os dias para a atividade A: '))
b = int(input('Informe os dias para a atividade B: '))
c = int(input('Informe os dias para a atividade C: '))
total = a + b + c

if a <0 or b < 0 or c <0:
    print('ERRO! os dias não podem ser negativos!')
else:
    print(f'Você tem {total} dias para fazer as atividades!')