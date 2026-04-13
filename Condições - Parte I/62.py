# dar uma olhada depois

def PA():

    primeiro = int(input("Digite o primeiro termo da PA: "))
    razao = int(input("Digite a razão da PA: "))

    termo_n = primeiro

    contador = 1 # se eu deixasse o 1 ele iria mostrar 11 termos 

    total = 0

    mais = 10

    while mais != 0:

        total = total + mais

        while contador <= total:

            print(f"{termo_n} -> ", end=" ")

            termo_n = termo_n + razao # ou termo_n += razão

            contador += 1

        print("PAUSA")

        mais = int(input("\nDigite mais quantos termos você gostaria de ver: "))

    print(f"Progressão finalizada com {total} termos mostrados")

    print("FIM DO PROGRAMA ")

    # Agora perguntar se o usuário quer mostrar mais alguns termos, o programa encerra quando ele quiser mostrar zero termos




PA()
