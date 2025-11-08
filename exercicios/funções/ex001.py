def calcular(ano_nasc, ano_atual):
    return ano_atual - ano_nasc

nascimento = int(input('Digite seu ano de nascimento: '))
atual = int(input('Digite o ano atual: '))
idade = calcular(nascimento, atual)
print(f'A idade é {idade} anos')
    