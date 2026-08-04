lista = []

maior = 0
maior_index = 0
maior = 0
menor_index = 0

for i in range(0,5):

    lista.append(int(input("Digite um valor: ")))

    if i == 0:

        maior = lista[0]
        menor = lista[0]

    else:

        if lista[i] > maior:

            maior = lista[i]
            maior_index = lista.index(lista[i])

        if lista[i] < menor:

            menor = lista[i]
            menor_index = lista.index(lista[i])

print(lista)
print(maior, maior_index)
print(menor, menor_index)

# maior = max(lista)
# print(maior, lista.index(maior) + 1)
# menor = min(lista)
# print(menor, lista.index(menor) + 1)

