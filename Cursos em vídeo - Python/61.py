def PA():

    a = int(input("Digite o primeiro termo da PA: "))
    r = int(input("Digite a razão da PA: "))

    termo = a

    i = 1

    while i <= 10:
        
        print(f"{termo} -> " ,end="")

        termo = termo + r

        i += 1



    # while y != 11:

    #     f = a + (y - 1) * r

    #     y += 1

    #     print(f)

PA()