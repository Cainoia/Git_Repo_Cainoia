from datetime import date


def idade():

    c = 0

    l = 0

    for i in range(0,7):

        x = int(input(f"Digite o {i + 1}º ano de nascimento: "))

        if date.today().year - x < 18:

            c += 1

        else:

            l += 1

    print(f"{l} pessoas são maior de idade e {c} são menores de idade")

idade()


