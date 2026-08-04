def fatorial():

    numero = int(input("Digite um número: "))

    cont = numero

    fatorial = 1

    while cont != 1:

        fatorial *= cont

        cont -= 1

    print(f"O fatorial de {numero} é {fatorial}")

fatorial()