# 7 - Utilize um loop for para calcular a soma dos números ímpares de 1 a 10.

num_impar = soma = 0
for c in range(1,11):
    if c % 2 ==1:
        num_impar += 1
        soma += c

print(f'Tem {num_impar} numeros impares e a soma é {soma}')



# INSTRUTORA: 
'''soma_impares = 0
for i in range(1, 11, 2):
    soma_impares += i
print(soma_impares)'''