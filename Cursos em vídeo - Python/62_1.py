def PA():

    primeiro = int(input("Digite o primeiro termo da PA: "))
    razao = int(input("Digite a razão da PA: "))

    contador = 1

    termo_n = primeiro

    mais_termos = 10

    total = 0

    while mais_termos != 0:

        total = total + mais_termos

        while contador <= total:

            termo_n += razao

            contador += 1

            print(termo_n)

        print("PAUSA")

        mais_termos = int(input("Quer digitar mais valores? "))

PA()