while True:
    nome = str(input('Nome de usuario: '))
    senha = str(input('Senha: '))

    if len(nome) < 5:
        print('A senha deve ter no minimo 5 caracteres!')
        continue

    if len(senha) < 8:
        print('A senha deve ter no minmo 8 caracteres!')
        continue
    else:
        print('Cadastro realizado com sucesso!')
        break
    


'''while True:
    nome_usuario = input("Digite seu nome de usuário: ")
    senha = input("Digite sua senha: ")

    if len(nome_usuario) < 5:
        print("O nome de usuário deve ter pelo menos 5 caracteres.")
        continue

    if len(senha) < 8:
        print("A senha deve ter pelo menos 8 caracteres.")
        continue

    print("Cadastro realizado com sucesso!")
    break'''

