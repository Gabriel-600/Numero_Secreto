peso = float(input('Digite seu peso: KG '))
altura = float(input('Digite sua altura: m '))
imc = peso / (altura**2)
print(f'Seu imc é {imc:.2f}')

if imc < 18.5:
    print('Abaixo do peso!')
elif 18.5 <= imc <25:
    print('Peso normal!')
elif imc >= 25:
    print('Acima do peso')


#INTRUTORA 
'''peso = float(input("Digite seu peso (kg): "))
altura = float(input("Digite sua altura (m): "))

imc = peso / (altura ** 2)
print(f"Seu IMC é: {imc:.2f}")

if imc < 18.5:
    print("Você está abaixo do peso.")
elif imc < 25:
    print("Você está com peso normal.")
else:
    print("Você está acima do peso.")'''