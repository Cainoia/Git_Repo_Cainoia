escolha_numero = 0

lista = []

decisao_continuar = ""

while True:

    escolha_numero = int(input("Digite um valor: "))

    if escolha_numero not in lista:

        lista.append(escolha_numero)

    decisao_continuar = str(input("Deseja continuar [Y/N]: ")).lower()

    if decisao_continuar in "n":

        print(sorted(lista))

        break

    