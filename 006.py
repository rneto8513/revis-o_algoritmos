# Crie um dicionário chamado “conta_bancaria” que contenha as seguintes propriedades:
#
# Nome do titular
# Número da conta
# Saldo
#
# Implemente as funções:
#
# depositar(conta: dict, valor: float): adiciona o valor ao saldo da conta.
# sacar(conta: dict, valor: float): subtrai o valor do saldo se houver fundos suficientes, retornando True em caso de sucesso e False caso contrário.


conta_bancaria = {"nome": "Raimundo", "número da conta": 8513, "saldo": 5000}

def depositar(conta, valor):
     conta["saldo"] += valor
     return conta

def sacar(conta, valor):
    if conta["saldo"] >= valor:
        conta["saldo"] -= valor
        return True
    else:
        print("não tem saldo suficiente ")
        return False


depositar(conta_bancaria, 100)
print(conta_bancaria)

sacar(conta_bancaria, 100)
print(conta_bancaria)