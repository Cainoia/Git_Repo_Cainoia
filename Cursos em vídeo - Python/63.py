# refazer, mas agora utilizando t1 = e t2 = 1

def sequencia():

    n_termos = int(input("Digite o número de termos desejados: "))

    t1 = 0

    t2 = 1

    contador = 3 

    print(f"{t1} -> {t2} -> ", end="")

    while contador <= n_termos:

        t3 = t2 + t1

        t1 = t2

        t2 = t3

        contador += 1

        print(f"{t3} -> " ,end="")

sequencia()