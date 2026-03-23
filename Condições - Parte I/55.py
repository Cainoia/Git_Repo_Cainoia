def peso():

    lista = []

    for i in range(0,5):

        w = int(input(f"Digite o {i + 1}º peso: "))
        lista.append(w)

    print(min(lista), max(lista))

peso()

