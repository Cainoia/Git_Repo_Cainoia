def programa():

    lista = ["somar", "multiplicar", "maior", "novos números", "sair do programa"]

    x = int(input("Digite um valor: "))
    y = int(input("Digite um valor: "))

    escolha = 0

    while escolha != 5:

        for i, base in enumerate(lista):
            print(f"[{i + 1}] -> {base}")

        escolha = int(input("Digite sua escolha: ")) #Se você deixasse o input fora do loop, o valor de escolha seria lido apenas uma vez. Se você digitasse 1, o while testaria 1 != 5 (Verdadeiro) e executaria o if escolha == 1 para sempre, pois o valor nunca mudaria.

        print("======================")


        if escolha == 1:

            print(f"A soma foi de {x + y}")

            print("======================")

        elif escolha == 2:

            print(f"A multiplicação foi de {x * y}")

            print("======================")


        elif escolha == 3:

            if x > y:

                maior = x
            
            else:

                maior = y

            print(f"O maior número foi {maior}")

            print("======================")

            

        elif escolha == 4:

            x = int(input("Digite um novo valor: "))
            y = int(input("Digite um novo valor: "))

            print("======================")

        

    print("Fim!\nMuito obrigado por ter usado o programa!")
            

programa()