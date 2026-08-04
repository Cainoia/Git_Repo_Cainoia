def frase():

    frase = str(input("Digite uma frase: ")).lower().strip() # strip() tira os espaços

    palavras = frase.split()                                 # transforma a frase em uma lista

    junto = "".join(palavras)                                # junto tudo tirando os espaços

    print(junto)

    inverso = ""

    for i in range(len(junto) -1, -1, -1):

        inverso += junto[i]

    print(inverso)

    if inverso == junto:

        print("É um palíndromo")
    
    else:

        print("NÃO um palíndromo")



frase()