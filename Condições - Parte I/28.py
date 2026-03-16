import random

def advinhar_numero():
    print("Pense num número de 1 a 5. Vou tentar adivinhar")
    
    for i in range(1):
        numero = int(input("Digite um número de 1 a 5:" ))

    numero_computador = random.randint(1,5)
    

    if numero == numero_computador:
        print(f"Eu acertei!, o número era {"\033[1;31;45m"}{numero_computador}{"\033[m"}")
    else:
        print(f"Desculpa, acabei errado, o número era {"\033[4;33;43m"}{numero_computador}{"\033[m"}")

advinhar_numero()