# Pensar melhor em como fazer, pois estou fazendo nas coxas já, sem usar dicionário nem lista nem tupla

#from datetime import date
#atual = date.today().year

def alistamento():

    for i in range(1):
        idade = int(input("Digite usa idade: "))
        print(f"sua idade é de {idade}")
    

    if idade < 18:
        print(f"Você ainda precisa se alistar\nFaltam {18 - idade} para você se alistar")
    elif idade == 18:
        print("Você precisa se alistar agora!")
    else:
        print(f"Você está atrasado para o alistamento!!\nVocê está atrasado {idade - 18} ano!")

    return idade

alistamento()

