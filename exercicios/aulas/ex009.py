'''9 - Solicite ao usuário um número e, em seguida, utilize um loop for para imprimir a tabuada desse número, indo de 1 a 10.'''



num = int(input('Quer ver a tabuada de qual numero?: '))

for c in range(1, 11):
    result = num * c
    print(f'{num} x {c} = {result}')





# INSTRUTORA: 
'''numero_tabuada = int(input("Digite um número para a tabuada: "))
for i in range(1, 11):
    resultado = numero_tabuada * i
    print(f"{numero_tabuada} x {i} = {resultado}")'''