def programa():

    from random import randint

    vitoria = 0

    jogador = 0

    escolha = 0

    lista = ["Par", "Impar"]

    while True:

        print("Escolha se vai com par ou ímpar: ")
        for index, base in enumerate(lista):
            print(f"{index + 1} : {base}")

        escolha = int(input("Digite sua escolha: "))

        while escolha not in [1, 2]:

            print("Você não escolheu se quer par ou ímpar")

            escolha = int(input("Digite sua escolha: "))
    
        print(30*"=")

        jogador = int(input("Digite um número: "))
        
        computador = randint(0, 10)

        print(f"Número do computador = {computador}")

        print(30*"=")

        if escolha == 1 and (computador + jogador) % 2 == 0:

            print("Parabens! Você ganhou")

            print(30*"=")

            vitoria += 1

        elif escolha == 2 and (computador + jogador) % 2 != 0:

            print("Parabens! Você ganhou")

            print(30*"=")

            vitoria += 1

        else:

            print("Você perdeu!")

            print(f"Você teve uma streak de {vitoria} vitórias")

            print(30*"=")

            break
        


programa()


        



