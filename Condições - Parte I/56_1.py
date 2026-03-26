def usuario():

    media = 0
    homem_mais_velho = 0
    nome_homem_mais_velho = ""
    mulheres_menor_de_20_anos = 0

    for i in range(4):
        print(f"===== {i + 1}ª Pessoa =====")
        nome = str(input("Digite o nome: "))
        idade = int(input("Digite a idade: "))
        sexo = str(input("Digite o sexo [M/F]: ")).lower()

        # Média de idade

        media += idade

        # Homem mais velho

        if i == 0 and sexo in "Mm":

            homem_mais_velho = idade
            nome_homem_mais_velho = nome

        if sexo in "Mm" and idade > homem_mais_velho:

            homem_mais_velho = idade
            nome_homem_mais_velho = nome

        # Mulheres com menos de 20 anos

        if sexo in "Ff" and idade < 20:

            mulheres_menor_de_20_anos += 1


    media = media / i
    
    print(media)
    print(nome_homem_mais_velho, homem_mais_velho)
    print(mulheres_menor_de_20_anos)

usuario()


