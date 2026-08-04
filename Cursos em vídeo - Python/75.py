lista = []

par = []

cont_9 = 0

pos_3 = 0

for i in range(0, 4):

    numero = int(input("Digite um valor: "))
    lista.append(numero)

tupla = tuple(lista)

for c in range(0, len(tupla)):

    if tupla[c] == 9:

        cont_9 += 1

    if tupla[c] % 2 == 0:

        par.append(tupla[c])

    if tupla[c] == 3:

        pos_3 = c

        

print(f"O número 9 apareceu {cont_9} vezes")
print(f"Número 3 -> {pos_3}")
print(f"{par} é par")





