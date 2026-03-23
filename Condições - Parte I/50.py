
def numero():

    s = 0               # inicializando o somatório

    for i in range(6):
        
        x = int(input(f"Digite um número: "))

        if x % 2 == 0:

            s += x

        print(f"[{i}] -> [{x}]\nResultado parcial = {s}")

    print(f"Resultado final = {s}")

numero()