def programa():

    idade = 0

    sexo = ""

    lista_idade = []
    lista_sexo = []

    maior_18 = 0
    homem = 0
    mulher_20 = 0

    while True:

        idade = int(input("Idade da pessoa a ser cadastrada: "))
        lista_idade.append(idade)
        sexo = str(input("Sexo da pessoa a ser cadastrada [M/F]: ")).upper()
        if sexo not in "MmFf":
            sexo = str(input("Sexo da pessoa a ser cadastrada [M/F]: ")).upper()
        lista_sexo.append(sexo)

        if idade > 18:
            maior_18 += 1

        if sexo in "Mm":
            homem += 1

        if sexo in "Ff" and idade < 20:
            mulher_20 += 1

        escolha = str(input("Deseja cadastrar mais uma pessoa: [Y/N]: ")).upper()

        if escolha not in "YyNn":

            escolha = str(input("Deseja cadastrar mais uma pessoa: [Y/N]: ")).upper()

        if escolha in "Nn":

            print(f"{maior_18} pessoas tem mais de 18 anos;\n{homem} homens foram cadastrados;\n{mulher_20} mulheres tem menos de 20 anos;")

            break

programa()





