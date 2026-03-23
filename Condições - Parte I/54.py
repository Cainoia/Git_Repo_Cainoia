from datetime import date

def idade():

    menor = 0
    
    maior = 0

    for i in range(0,7):

        ano = int(input(f"Digite o {i + 1}º ano de nascimento: "))

        age = date.today().year - ano

        # print(ano, age)

        if age < 18:

            menor += 1

        else: 

            maior += 1

    print(f"Quantidade de pessoas menores de 18 anos: {menor}\nQuantidade de pessoas maiores de 18 anos: {maior}")



idade()