# implemente um dicionario chamado "produto" que represente um item no estoque de uma loja com as seguintes propriedades:
# nome do produto, quantidade em estoque, preço unitario
# crie uma função "atualize_estoque" que recebe o dicionario do produto e some a quantidade informada ao estoque,
# após isso, retorne o produto  atualizado e imprima na tela

produto = {
    "nome": "notebook",
    "quantidade": 10,
    "preco": 2.5000
}

def atualizar_estoque(produto,quantidade):
    produto["quantidade"] += quantidade
    return produto


print(atualizar_estoque(produto, 2))
