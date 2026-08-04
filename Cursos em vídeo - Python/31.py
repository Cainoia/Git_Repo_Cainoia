def custo_viagem():
    x = int(input("Qual a distância da sua viagem?"))
    if x <= 200:
        print(f"O preço da passagem será de {x*0.50}")
    else:
        print(f"O preço da passagem será de {x*0.45}")

# Dava pra ter criado somente uma variavel x dentro do if else e dps um print foram com f"(O preço é {x})"

custo_viagem()
        