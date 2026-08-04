
# Poderia ter usado a biblioteca datetime eu acho

# from datetime import date => ano_atual = date.today().year

# Formas de usar datetime
# print(date.today())              # 2024-XX-XX
# print(date.today().year)         # 2024
# print(date.today().month)        # mês atual
# print(date.today().day)          # dia atual


def ano_nascimento():

    lista = []

    for i in range(1):
        ano = int(input("Digite o seu ano de nascimento: "))
        lista.append(ano)

    if 2025 - lista[0]  <= 9:
        print("Categoria Mirim")
    elif 2025 - lista[0]  > 9 and 2025 - lista[0] <= 14:
        print("Categoria Infantil")
    elif 2025 - lista[0]  > 14 and 2025 - lista[0] <=  19:
        print("Categoria Junior")
    elif 2025 - lista[0]  > 19 and 2025 - lista[0] <=  20:
        print("Categoria Sênior")
    else:
        print("Categoria Master")


ano_nascimento()