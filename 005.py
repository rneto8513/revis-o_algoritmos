# Crie uma lista chamada “catalogo” que contenha dicionários representando filmes. Cada dicionário deve conter:
#
# Título
# Ano de lançamento
# Gênero
#
# Implemente uma função “filtrar_por_genero(catalogo: list, genero: str)” que recebe a lista de filmes e retorna apenas
# os filmes que pertencem ao gênero informado. Após retornar, imprima-os em tela.

catalogo = [{"titulo":"interestelar", "ano de lançamento": 2014, "gênero": "ficção cientifica"},
            {"titulo": "django livre", "ano de lançamento": 2012, "gênero": "faroeste"},
            {"titulo": "a lista de schindler", "ano de lançamento": 1994, "gênero": "drama"},
            {"titulo": "super bad", "ano de lançamento": 2007, "gênero": "comédia"}]


def fitrar_por_catalogo(catalogo, genero):
    filtro = []

    for filme in catalogo:
        if filme["gênero"] == genero:
            filtro.append(filme)

    if filtro:
        for filme in filtro:
            print(f"Titulo: {filme["titulo"]}")
            print(f"ano de lançamento: {filme["ano de lançamento"]}")
            print(f"gênero: {filme["gênero"]}")
    else:
        print(f"não tem filmes do gênero escolhido")


fitrar_por_catalogo(catalogo, "comédia")