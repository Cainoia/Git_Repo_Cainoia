def pa():

    numero = int(input("Digite um número: "))

    razao = int(input("Digite a razão da PA: "))

    contador = 1


    while contador != 10:

        contador += 1

        numero += razao

    print(numero)

    escolha = 1

    while escolha != 0:

        escolha = int(input("Gostaria de ver mais quantos termos: "))

        numero += razao





pa()



