
def triangulo():

    lados = []

    for i in range(3):

        x = int(input(f"Digite o {i + 1}º lado: "))

        lados.append(x)

    a, b, c = lados[0], lados[1], lados[2] # gostei de poder transformar a lista em variáveis


    if (a + b > c) and (a + c > b) and (b + c > a):

        print(f"O triâgulo de lados {lados} é possível")

        print(f"=========Pensando em que tipo de triânguilo pode ser=============")

        if (a == b == c):

            print("O triângulo é \033[4:mEquilátero")

        elif (a == b) or (b == c) or (a == c):

            print("O triângulo é \033[4:mIsóceles")

        elif (a != b != c):

            print("O triângulo é \033[4:mEscaleno")

    else:

        print(f"O triâgulo de lados {lados} \033[4;34mNÃO\033[m é possível")


triangulo()


