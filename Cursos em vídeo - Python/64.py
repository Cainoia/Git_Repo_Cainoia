def programa():

    numero = 0

    contador = 0

    soma = 0

    # numero = contador = soma = 0

    numero = int(input("Digite um número: "))

    while numero != 999:

        contador += 1

        soma += numero

        numero = int(input("Digite um número: "))   # Adicionar a flag dentro do while (Não entendi)

    print(f"A quantidade de números digitados foi = {contador}")
    print(f"A soma entre os números foi = {soma}")


programa()



