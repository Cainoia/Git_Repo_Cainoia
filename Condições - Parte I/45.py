
# esse código aqui é de mongoloide mds

import random

def jokenpo():

    lista = ["pedra", "papel", "tesoura"]

    for i, base in enumerate(lista):
        print(f"[{i + 1}] {base}")

    minha_escolha = int(input("Digite sua escolha, com base na tabela acima: "))

    computador = random.choice(lista) #.choice escolhe um valor aleatório da lista

    if minha_escolha == 1 and computador == "pedra":                                  #poderia ter feito um if dentro de um if
        print(f"Os dois escolheram {lista[0]}!\nVocês empataram!")

    elif minha_escolha == 1 and computador == "papel":
        print(f"Você perdeu")

    elif minha_escolha == 1 and computador == "tesoura":
        print(f"Você ganhou!")

    elif minha_escolha == 2 and computador == "pedra":
        print(f"Você ganhou!")

    elif minha_escolha == 2 and computador == "papel":
        print(f"Os dois escolheram {lista[1]}!\nVocês empataram!")

    elif minha_escolha == 2 and computador == "tesoura":
        print(f"Você perdeu")

    elif minha_escolha == 3 and computador == "pedra":
        print(f"Você perdeu")

    elif minha_escolha == 3 and computador == "papel":
        print(f"Você ganhou!")

    elif minha_escolha == 3 and computador == "tesoura":
        print(f"Os dois escolheram {lista[2]}!\nVocês empataram!")

    print(f"A escolha do jogador foi {minha_escolha}")
    
    print(f"A escolha do computador foi {computador}")

jokenpo()
    