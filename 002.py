# escreva uma função separa_pares_impares que recebe uma lista de números inteiros e retorna duas listas: uma contendo
# os números pares e outra contendo os números impares


def separa_pares_impares(numeros):
    numeros_impares = []
    numeros_pares = []
    for i in numeros:
        if i % 2 == 0:
            numeros_pares.append(i)
        elif i % 2 != 0:
            numeros_impares.append(i)
    return numeros_pares, numeros_impares
    print(numeros_pares)
    print(numeros_impares)

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(separa_pares_impares(numeros))
