def sequencia():

    numero = int(input("Digite um número: "))

    t1 = 0

    t2 = 1

    contador = 2

    print(f"{t1} -> {t2} -> ", end="")

    while contador != numero:

        t3 = t2 + t1
        
        print(f"{t3} -> ", end="")

        t1 = t2

        t2 = t3

        contador += 1


sequencia()

    

