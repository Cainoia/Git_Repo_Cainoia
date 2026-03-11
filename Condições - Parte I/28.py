import random

def advinhar_numero():
    print("Pense num número de 1 a 5. Vou tentar adivinhar")
    numero_computador = random.randint(1,5)
    x = int(input("Digite um número de 1 a 5:" ))

    if x == numero_computador:
        print(f"Eu acertei!, o número era {numero_computador}")
    else:
        print(f"Desculpa, acabei errado, o número era {numero_computador}")

advinhar_numero()