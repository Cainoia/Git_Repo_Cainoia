def programa():

    soma = 0
    mais_1000 = 0
    mais_barato = 0

    lista_nome = []
    lista_preco = []

    while True:

        nome = str(input("Digite o nome do produto: "))
        lista_nome.append(nome)
        preco = float(input("Digite o preco do produto: "))
        lista_preco.append(preco)
        
        soma += preco

        if preco > 1000:
            mais_1000 += 1


        escolha = str(input("Desejar continuar [Y/N]: "))

        if escolha not in "YyNn":

            escolha = str(input("Desejar continuar [Y/N]: "))

        if escolha in "Nn":

            # Comparar com um valor absoluto

            mais_barato = lista_preco[0]

            for i in range(0, len(lista_preco)):
                
                if lista_preco[i] < mais_barato:

                    mais_barato = lista_preco[i]

            index = lista_preco.index(mais_barato)

            nome_produto_mais_barato = lista_nome[index]

            print(f"{soma} reais no total gasto;\n{mais_1000} produtos mais que 1000 reais;\n{nome_produto_mais_barato} é o produto mais barato;")

            break

programa()