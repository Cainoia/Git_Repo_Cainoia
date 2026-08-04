def imc():

    peso_altura = []
    

    for i in range(1):
        peso = int(input("Digite o seu peso (kg): "))
        altura = float(input("Digite a sua altura (m): "))
        peso_altura.extend([peso, altura])

    w, h = peso_altura[0], peso_altura[1]

    indice = w / (h ** 2)

    print(round(indice))

    if indice < 18.5:

        print("Abaixo do peso")

    elif indice >= 18.5 and indice < 25:

        print("Peso ideal")

    elif indice >= 25 and indice < 30:

        print("Sobrepeso")

    elif indice >= 30 and indice < 40:

        print("Obesidade")

    else:

        print("Obesidade mórbida")

imc()