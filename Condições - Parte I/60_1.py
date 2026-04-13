def fatorial():

    numero = int(input("Digite um número: "))

    fatorial = 1

    contador = numero

    while contador != 0:

        fatorial *= contador

        contador -= 1

        print(fatorial, contador)

fatorial()