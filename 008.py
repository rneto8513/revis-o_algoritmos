# Implemente um dicionário “contato” que represente uma pessoa na lista “agenda_telefonica” com as seguintes informações:
#
# Nome
# Telefone
# Email
#
# Crie uma função buscar_contato(agenda_telefonica: list, nome: str) que recebe uma lista de contatos e retorna o
# contato correspondente ao nome fornecido ou None caso não exista.

def buscar_contato(agenda_telefonica, nome):
    for contato in agenda_telefonica:
        if contato["nome"] == nome:
            return contato


agenda_telefonica = [{"nome": "Arthur", "telefone": 1234-5678, "email": "art@gmail.com"},
                     {"nome": "Raimundo", "telefone": 5521-4369, "email": "ramud@gmail.com"}]


resultadoDaBusca = buscar_contato(agenda_telefonica, "Raimundo")
print(resultadoDaBusca)