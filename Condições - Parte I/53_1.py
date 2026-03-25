def frase():

    frase = str(input("Digite uma frase: ")).lower().strip()

    palavras = frase.split()

    junto = "".join(palavras)

    print(junto)

    inverso = ""

    for i in range(len(junto) -1, -1, -1):

        inverso += junto[i]

        print(inverso)




frase()