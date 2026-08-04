
def pa():

    s = 0

    for i in range(1):

        x = int(input("Digite o primeiro termo da PA: "))
        y = int(input("Digite a razão da PA: "))

    for c in range(1, 11):

        a = x + (c - 1) * y

        s += a # aqui realizei o somatório da PA

        print(a, end=" ")
    
    print(f"\nSomatório da PA = {s}")

pa()