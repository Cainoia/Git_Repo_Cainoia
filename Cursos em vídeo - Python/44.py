def valor():

    lista = ["à vista, dinheiro ou cheque", "à vista, no cartão", "até 2x no cartão", "3x ou mais no cartão"]

    for i, base in enumerate(lista):

        print(f"[{i + 1}] {base}") # i + 1 pois o i começa em 0

    x = int(input("Digite a opção desejada: "))

    if x == 1:
        print("10% de desconto")

    elif x == 2:
        print("5% de desconto")

    elif x == 3:
        print("Preço normal")

    elif x == 1:
        print("20% de juros")

valor()