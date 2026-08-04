def caixa():

    valor = int(input("Qual o valor a ser sacado: "))

    saque = valor

    for i in [50, 20, 10, 1]:

        quantidade = saque // i

        saque %= i

        if quantidade > 0:

            print(f"{quantidade} de cédulas de R$ {i}")

caixa()