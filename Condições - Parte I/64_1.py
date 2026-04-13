def programa():

    numero = int(input("Digite um número: "))

    contador = 0

    soma = 0

    while numero != 999:

        contador += 1

        soma += numero

        numero = int(input("Digite um número: "))

    print(f"{soma} e {contador}")

programa()