distancia = float(input('Digite a distancia percorrida (em km): '))

if distancia <= 100:
    print('Valor do pedagio R$10,00')
elif 100 < distancia <= 200:
    print('Valor do pedagio R$20,00')
else:
    print('Valor do pedagio R$30,00')