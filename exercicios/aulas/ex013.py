'''2 - Utilizando o dicionário criado no item 1:

Modifique o valor de um dos itens no dicionário (por exemplo, atualize a idade da pessoa);
Adicione um campo de profissão para essa pessoa;
Remova um item do dicionário.
'''


pessoa = {'nome':'bielzin', 'idade': 18, 'cidade': 'Brasilia'}
pessoa['idade'] = 19

pessoa['profissão'] = 'Programador'
pessoa.pop('cidade')

print(pessoa)




#INSTRUTORA
'''# Atualização de Idade
pessoa['idade'] = 31

# Adicionando Profissão
pessoa['profissao'] = 'Engenheiro'

# Remoção de Elemento
del pessoa['cidade']'''