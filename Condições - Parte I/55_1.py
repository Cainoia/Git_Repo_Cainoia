def peso():

    maior = 0
    menor = 0
    
    for i in range(5):

        x = float(input(f"Digite o {i + 1}º peso (em kg): "))

        if i == 0:

            maior = x
            menor = x

        else:

            if x > maior:           # condição de descobrir o maior

                maior = x

            if x < menor:           # condição de descobrir o menor

                menor = x

    print(f"O maior peso lido goi {maior} e o menor peso foi {menor}")

    

peso()