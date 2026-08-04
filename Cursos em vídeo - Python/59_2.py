def programa():

    lista = []

    for i in range(1, 3):
        
        numero = int(input("Digite um número: "))
        lista.append(numero)

    #print(lista)

    numero_1 = lista[0]
    numero_2 = lista[1]

    lista_1 = ["Somar", "Multiplicar", "Maior", "Novos números", "Sair do programa"]

    escolha = 0

    while escolha != 5:

        for i, base in enumerate(lista_1):

            print(f"{i+1} : {base}")

        escolha = int(input("Digite a operação que quer realizar: \n"))

        if escolha == 1:

            print(f"A soma de {numero_1} + {numero_2} = {numero_1 + numero_2}\n")

        elif escolha == 2:

            print(f"A multiplicação de {numero_1} * {numero_2} = {numero_1 * numero_2}\n")

        elif escolha == 3:

            if numero_1 > numero_2:

                maior = numero_1

            else:

                maior = numero_2

            print(f"O maior valor entre {numero_1} e {numero_2} é {maior} \n")

        elif escolha == 4:

            numero_1 = int(input("Digite o novo 1º numero: "))
            numero_2 = int(input("Digite o novo 2º numero: "))

    print("FIM DO PROGRAMA")    


programa()