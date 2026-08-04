listagem = ("Lapis", 5, "Caderno", 30, "Borracha", 3, "Caneta", 4.5, "Estojo", 15.75, 
            "Régua", 12.5)

for c in range(0, len(listagem)):

    if c % 2 == 0:

        print(f"{listagem[c]:.<30}", end="")

    else:

        print(f"R$ {listagem[c]:>5.2f}")