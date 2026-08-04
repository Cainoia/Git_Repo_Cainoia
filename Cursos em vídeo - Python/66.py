def programa():

    numero = 0
    soma = 0
    contador = 0

    while True:

        numero = int(input("Digite um número: "))

        if numero == 999:

            break

        contador += 1

        soma += numero

    print(f"A soma foi de {soma}\nA quantidade de números foi {contador}")
programa()