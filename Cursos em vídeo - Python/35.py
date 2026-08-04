def analize_triangulo():

    triangulo_lados = []

    for i in range(3):
        lado = float(input(f"Digite o {i + 1}º comprimento: "))
        triangulo_lados.append(lado)

    if triangulo_lados[0] + triangulo_lados[1] > triangulo_lados[2] and triangulo_lados[0] + triangulo_lados[2] > triangulo_lados[1] and triangulo_lados[1] + triangulo_lados[2] > triangulo_lados[0]:
        print(f"O triângulo com os comprimentos {triangulo_lados} é possível!")
    else:
        print(f"O triângulo com os comprimentos {triangulo_lados} NÃO é possível!")

analize_triangulo()