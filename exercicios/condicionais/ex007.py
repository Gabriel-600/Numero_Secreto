num1 = float(input('Digite a 1ª nota: '))
num2 = float(input('Digite a 2ª nota: '))
num3 = float(input('Digite a 3ª nota: '))
media = (num1 + num2 + num3) / 3

print(f'A media foi {media:.2f}')

if media >= 7:
    print('Aprovado!') 
elif 5 <= media <7:
    print('Recuperação!')
elif media <5:
    print('Reprovado!')



#INSTRUTORA 
'''nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

media = (nota1 + nota2 + nota3) / 3

if media >= 7:
    print("Aprovado")
elif 5 <= media < 7:
    print("Recuperação")
else:
    print("Reprovado")'''