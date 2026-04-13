def programa():

    numero = 0

    media = 0

    soma = 0

    maior = 0

    menor = 0

    contador = 0

    pergunta = " "

    while pergunta not in "Nn":

        numero = int(input("Digite um valor: "))

        contador += 1

        soma += numero

        if contador == 1:

            maior = menor = numero

        else:

            if numero > maior:

                maior = numero

            if numero < menor:

                menor = numero

        pergunta = str(input("Você quer continuar a digitar valores [S/N]: ")).lower().strip()[0]


    media = soma / contador

    print(f"A soma dos números foi = {soma}")
    print(f"A quatidade de números foi = {contador}")
    print(f"A média dos números foi = {media}")
    print(f"O maior número foi = {maior}")
    print(f"O menor número foi = {menor}")

programa()

