# Melhoria do desafio 28

from random import randint

def pensar():

    numero = randint(0,10)

    cont = 0

    tentativa = int(input("Tente adivinhar o número: "))

    while tentativa != numero:

        cont += 1

        tentativa = int(input("Você errou!\nTente denovo: "))

    print(f"Parabens, o número era {numero}!\nVocê levou {cont} tentativas para acertar")

pensar()