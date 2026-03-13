# Utilizando dicionários

def maior_menor():

    numeros = {}

    for i in range(3):

        valor = int(input(f"Digite o {i + 1}º numero: "))
        numeros[f"n{i + 1}"] = valor


    print(numeros["n1"], numeros["n2"], numeros["n3"])

    maior = numeros["n1"]

    if numeros["n2"] > numeros["n1"] and numeros["n2"] > numeros["n3"]:
        maior = numeros["n2"]
    if numeros["n3"] > numeros["n1"] and numeros["n3"] > numeros["n2"]:
        maior = numeros["n3"]

    menor = numeros["n1"]

    if numeros["n2"] < numeros["n1"] and numeros["n2"] < numeros["n3"]:
        menor = numeros["n2"]
    if numeros["n3"] < numeros["n1"] and numeros["n3"] < numeros["n2"]:
        menor = numeros["n3"]
    
    # Utilizando a função min e max do dicionário
    # 
    # maior = max(numeros.values())
    # menor = min(numeros.values())
    # print(f"O maior valor é {maior} e o menor valor é {menor}")
     
     

    print(f"O maior valor é {maior} e o menor valor é {menor}")


maior_menor()