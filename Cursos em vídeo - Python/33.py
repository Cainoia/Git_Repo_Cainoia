# Utilizando um loop de listas


def encontrar_maior(lista_numeros):
    
    maior = lista_numeros[0]

    for numero in lista_numeros:
        if numero > maior:         # se o numero for maior que o maior atual
            maior = numero         # o maior atual é atualizado
    
    return maior                   # salvar o maior valor


def encontrar_menor(lista_numeros):

    menor = lista_numeros[0]

    for numero in lista_numeros:
        if numero < menor:
            menor = numero

    return menor

def main():

    numeros = []

    for i in range(3):
        numero = float(input(f"Digite o {i + 1}º número:"))
        numeros.append(numero)
    
    maior_numero = encontrar_maior(numeros)
    menor_numero = encontrar_menor(numeros)

    print(f"Os numeros digitados foram: {numeros}")
    print(f"O maior numero foi {maior_numero}")
    print(f"O menor numero foi {menor_numero}")


main()
    


