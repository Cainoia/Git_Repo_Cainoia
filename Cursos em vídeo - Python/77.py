tupla = ("aprender", "estudar", "trabalhar")

for i in tupla:

    print(f"\nA palavra {i.upper()} possui as vogais", end= " ")

    for letra in i:

        if letra.lower() in "aeiou":

            print(letra, end= " ")