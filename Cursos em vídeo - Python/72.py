from num2words import num2words

def tupla():

    tupla = tuple(range(21))

    escolha = int(input("Digite o valor de 0 a 20 que deseja saber a posição: "))

    for c in tupla:

        if escolha not in tupla:

            print("Digite um valor novamente!")

            print("="*30)

            escolha = int(input("Digite o valor de 0 a 20 que deseja saber a posição: "))

    print(f"Você escolheu o número {num2words(escolha, lang = "pt_BR")}")


tupla()