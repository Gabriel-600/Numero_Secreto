'''3 - Solicite um nome de usuário e uma senha e use uma estrutura if else para verificar se o nome de usuário e a senha fornecidos correspondem aos valores esperados determinados por você.'''

usuario_certo = 'bielzin'
senha_certa = 'jhujhu123'

nome = str(input('Usuario: '))
senha = str(input('Senha: '))


if nome == usuario_certo and senha == senha_certa:
    print('Login feito com sucesso!')
else:
    print('Erro! tente novamente.')



#INSTRUTORA: 
'''usuario_correto = "alura"
senha_correta = "alura123"

usuario = input("Digite o nome de usuário: ")
senha = input("Digite a senha: ")

if usuario == usuario_correto and senha == senha_correta:
    print("Login bem sucedido!")
else:
    print("Credenciais inválidas. Tente novamente.")'''