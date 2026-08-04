def caixa():

    valor = int(input("Qual o valor a ser sacado: "))

    cedula = 50

    saque = valor

    total_cedula = 0

    while True:

        if saque > cedula:

            saque -= cedula

            total_cedula += 1

        else:

            if cedula == 50:

                cedula = 20

            elif cedula == 20:

                cedula = 10

            elif cedula == 10:

                cedula = 1

            if saque == 0:

                break








