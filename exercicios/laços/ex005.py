projetos = ["website", "jogo", "análise de dados", None, "aplicativo móvel"]

for p in projetos:
    if p is None:
        print('Projeto ausente')
    else:
        print(p)