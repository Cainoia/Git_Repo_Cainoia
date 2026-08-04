def numero():

    lista_numero = []

    for i in range(2):
        x = int(input(f"Digite o {i+1}º número: "))
        lista_numero.append(x)

    print(f"O números selecionados foram {lista_numero[0]} e {lista_numero[1]}")

    if lista_numero[0] > lista_numero[1]:
        print(f"O primeiro valor {lista_numero[0]} é maior que o segundo valor {lista_numero[1]}")

    elif lista_numero[1] > lista_numero[0]:
        print(f"O segundo valor {lista_numero[1]} é maior que o primeiro valor {lista_numero[0]}")

    else:
        print("Os dois valores sõa iguais")

numero()

