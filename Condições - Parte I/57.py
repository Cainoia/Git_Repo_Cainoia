def sexo():

    sexo = str(input("Digite o sexo: ")).upper().strip()[0]     # strip: eliminar vários espaços, [0]: pegar somente a primeira letra

    while sexo not in "MF":

        sexo = str(input("Dados inválidos. Informe seu sexo: ")).upper().strip()[0]

    print(f"O seu sexo é {sexo}")

sexo()
