import math

def tabuada():

    numero = 0

    while True:

        numero = int(input("Digite um número: "))

        if numero < 0:

            break

        lista = []

        for i in range(1, 11):

            valor = i * numero

            lista.append(valor)

        for index, base in enumerate(lista):

            print(f"{index + 1} * {numero} : {base}")


tabuada()



        