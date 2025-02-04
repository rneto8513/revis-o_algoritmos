# Crie um dicionário chamado “livro” que represente um livro em uma biblioteca com as seguintes propriedades:
#
# Título
# Autor
# Ano de publicação
# Quantidade de cópias disponíveis
#
# Implemente uma função emprestar_livro(livro: dict) que reduz a quantidade de cópias disponíveis em 1 se houver
# exemplares disponíveis, retornando True se o empréstimo for bem-sucedido e False caso contrário.


livro = {"nome": "fireheart 451", "autor": "fireheart 451", "ano de publicação": "1953", "quantidade": 5}


def emprestar_livro(livro):
    livro["quantidade"] -= 1
    return livro


emprestar_livro(livro)
print(livro)