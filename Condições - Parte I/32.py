def ano_bissexto():
    x = int(input("Digite o ano que você quer saber: "))
    if x % 4 == 0 and x % 400 == 0:
        print(f"O ano {x} é bissexto")
    else:
        print(f"O ano {x} não é bissexto")

ano_bissexto()
        