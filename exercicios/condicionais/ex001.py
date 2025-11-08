banana = int(input('Quantas bananas foram vendidas?: '))
maca = int(input('Quantas maças foram vendidas?: '))

if banana > maca:
    print('Banana vendeu mais!')
elif maca > banana:
    print('Maça vendeu mais!')
else:
    print('Deu empate!')