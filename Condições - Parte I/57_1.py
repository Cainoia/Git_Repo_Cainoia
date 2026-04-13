def sexo():

    sexo = str(input("Digite um sexo [M/F]: ")).lower().strip()

    while sexo not in "MmFf":

        sexo = str(input("Digite um valor aceito [M/F]: "))

sexo()

