import random

def desafio28():

    computador = random.randint(0,10)

    numero = int(input("Digite um número: "))

    contador = 1

    while numero != computador:

        numero = int(input("Você errou! Digite outro número: "))

        contador += 1

    print(f"Parabens! Você acertou!\nO número era {computador}")
    print(f"Foram necessários {contador} palpites para acertar")


desafio28()