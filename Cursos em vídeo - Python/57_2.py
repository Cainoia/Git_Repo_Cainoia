def sexo():

    sexo = str(input("Digite seu sexo [M/F]: "))

    while sexo not in "MmFf":
 
        sexo = str(input("Digite seu sexo [M/F]: "))

    print(f"Seu sexo é \n{sexo}")

sexo()