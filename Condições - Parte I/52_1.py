# Ideia: Número primo é divisível por 1 e por ele mesmo, o contador c precisa ser igual a 2


def primo():

    x = int(input("Digite um número: "))

    c = 0

    for i in range(1, x + 1):

        y = x / i

        print(y)

        if x % i == 0:

            c += 1

    if c == 2:

        print(f"O número {x} é primo")

    else:

        print(f"O número {x} NÃO é primo")

primo()

            