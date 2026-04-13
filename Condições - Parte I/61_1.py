def desafio51():

    primeiro = int(input("Digite o primeiro termo da PA: "))
    razao = int(input("Digite a razão da PA: "))

    termo_n = primeiro

    contador = 1

    while contador <= 10:
        
        print(termo_n)
        
        termo_n += razao # termo_n = termo_n (primeiro) + razão

        contador += 1

desafio51()
    