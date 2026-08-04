def caixa():

    valor = int(input("Qual o valor a ser sacado: "))

    cedula = [1, 10, 20, 50]

    saque = valor

    total_1  = 0
    total_10 = 0
    total_20 = 0
    total_50 = 0

    while saque != 0:

        print("="*30)

        print(f"O valor a ser sacado foi {valor}")

        if valor % cedula[3] == 0:

            total_50 = valor / cedula[3]

            saque = valor % cedula[3]

            print(f"{total_50} notas de 50 reais")

        if saque % cedula[2] == 0:

            total_20 = saque / cedula[2]

            saque = saque % cedula[2]

            print(f"{total_20} notas de 20 reais")

        if saque % cedula[1] == 0:

            total_10 = saque / cedula[1]

            saque = saque % cedula [1]

            print(f"{total_10} notas de 10 reais")

        if saque % cedula[0] == 0:

            total_1 = saque / cedula[0]

            saque = saque % cedula[0]

            print(f"{total_1} notas de 1 real")



caixa()

