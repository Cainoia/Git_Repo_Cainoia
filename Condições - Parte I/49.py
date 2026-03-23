

def tabuada():

    lista = []

    for c in range(1):

        numero = int(input("Digite o número desejado para vizualizar a tabuada: "))

    for i in range(1, 11):

        s = numero * i

        lista.append(s)

        print(f"[{numero} X {i}] = {s}")


#    for i, base in enumerate(lista):
#
#        print(f"{i + 1} [{lista}]")

tabuada()