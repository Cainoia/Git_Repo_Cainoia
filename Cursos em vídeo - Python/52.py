# Esse a gabi me ajudou a fazer


def primo():

    numero = int(input("Digite um número: "))

    c = 0

    for i in range(1, numero + 1):    # Tem que começar no 1 devido a i que tem que começar no 1, pois se for 0 a primeira divisão ocorre com i == 0

        if numero % i == 0:

            c += 1                    # Adiconar 1 ao somatório 

    if c == 2:                        # condição de primo que só pode ser divisivel por ele mesmo e por 1

        print(f"{numero} é primo")
    else:
            
        print(f"{numero} é \033[4;34mNÃO\033[m primo")
    

primo()