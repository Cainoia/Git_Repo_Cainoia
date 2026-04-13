def programa():

    numero = 0

    maior = menor = numero

    contador = 0

    soma = 0

    escolha = " "

    while escolha not in "Nn":

        numero = int(input("Digite um número: "))
        
        soma += numero

        contador += 1

        if contador == 1: # Condição para primeiro loop

            maior = menor = numero

        else:

            if numero > maior:

                maior = numero

            if numero < menor:

                menor = numero

        escolha = str(input("Você deseja continuar ainda [S/N]: ")).lower().strip()


    media = soma / contador

    print(f"A média foi {media}")
    print(f"A soma foi {soma}")
    print(f"O maior valor foi {maior}")
    print(f"O menor valor foi {menor}")


programa()