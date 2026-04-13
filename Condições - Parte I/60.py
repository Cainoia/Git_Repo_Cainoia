def numero_fatorial():

    x = int(input("Digite um número: "))

    y = x

    z = 1

    while y != 0:

        z *= y

        y -= 1  # y -= 1

        print(y)

    print(f"O valor de {x}! = {z}")

numero_fatorial()