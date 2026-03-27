import random

def advinhar_numero():

    n_adv = 0

    computador = random.choice(range(0,11))
    # computador = random.randint(1,5)

    for i in range(1):

        n = int(input("Digite o valor que acha certo: "))

    while n != computador:

        n = int(input("Você errou. Digite um outro número: "))

        n_adv += 1

    print(f"Você acertou, o número era {computador}\nDemorou {n_adv} tentativas!")

    # if n == computador:

    #     print(f"Você acertou, o número era {computador}")
        
    # else:
        
    #     print(f"Você errou, o número era {computador}")

advinhar_numero()