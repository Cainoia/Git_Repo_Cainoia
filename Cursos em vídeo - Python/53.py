def palindromo():

    frase = str(input("Digite sua frase: ")).lower().strip() # poderia usar o .strip() para tirar os espaços

    palavras = frase.split()                                 # separa tudo em elementos da lista, no caso cada palavra é um elemento

    junto = "".join(palavras)

    print(junto)

    # como fazer a varredura de tras para frente da lista

    inverso = ""                                             # É assmim que você para o caso de str

    for i in range(len(junto) - 1, -1, -1):                  # o range vai de trás para frente, onde o começo é o comprimento da "lista" só que - 1, pois o se a lista tem 10 elementos, o ultimo elemento dela é 9, até o 0, mas como você quer pegar o 0 também, a varredura tem que ir até -1 , e -1 de passo pois você quer a varredura de trás para frente

        # print(junto[i]) 
        
        inverso += junto[i]

    if inverso == junto:                                 # Como o if esta dentro do for, ele faz o teste cada a quantidade i de vezes especificas no range

            # print(f"A frase {junto}, com inverso = {inverso} \nÉ {"\033[4;35m"}PALÍNDROMO{"\033[m"}!")
        print(f"É {"\033[4;35m"}PALÍNDROMO{"\033[m"}!")

    else: 

            # print(f"A frase {junto}, com inverso = {inverso} \n{"\033[1;36m"}NÃO{"\033[m"} é {"\033[4;35m"}PALÍNDROMO{"\033[m"}!")
        print(f"{"\033[1;36m"}NÃO{"\033[m"} é {"\033[4;35m"}PALÍNDROMO{"\033[m"}!")


    # print(junto, inverso)


palindromo()