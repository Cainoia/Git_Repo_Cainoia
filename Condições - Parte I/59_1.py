def programa():

    lista = ["SOMAR", "MULTIPLICAR", "MAIOR", "NOVOS NÚMEROS", "SAIR DO PROGRAMA"]

    valor_1 = int(input("Digite um valor: "))
    valor_2 = int(input("Digite um valor: "))


    escolha = 0

    while escolha != 5:

        for i, base in enumerate(lista):

            print(f"[{i + 1}] : {base}")

        escolha = int(input("Digite a sua escolha: "))

        if escolha == 1:

            soma = valor_1 + valor_2

            print(f"A soma deu {soma}")

        if escolha == 2:

            multi = valor_1 * valor_2

            print(f"A multiplicação deu {multi}")

        if escolha == 3:

            if valor_1 > valor_2:

                maior = valor_1


            else:

                maior = valor_2

            print(f"O maior foi {maior}")

        if escolha == 4:

            print("Digite os novos números abaixo")

            valor_1 = int(input("Digite um valor: "))
            valor_2 = int(input("Digite um valor: "))
    
    print("FIM DO PROGRAMA")



programa()

