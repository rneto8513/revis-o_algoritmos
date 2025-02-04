# Crie uma lista “carrinho” onde cada “item” seja um dicionário representando um produto com as chaves:
#
# Nome
# Preço
# Quantidade
#
# Implemente uma função calcular_total(carrinho: list) que retorna o valor total da compra.



carrinho = [
    {"nome": "mouse", "preço": 100, "quantidade": 5},
    {"nome": "teclado", "preço": 150, "quantidade": 3}]

def calcular_total(carrinho):
    total = 0
    for item in carrinho:
        total += item["preço"] * item["quantidade"]
    return total


print(calcular_total(carrinho))