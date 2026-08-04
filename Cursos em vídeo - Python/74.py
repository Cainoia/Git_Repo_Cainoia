from random import randint

lista = []

for i in range(0, 5):

    lista.append(randint(0,10))

print(lista)

tupla = tuple(lista)

print(tupla)

print(f"O menor valor foi {min(tupla)}")
print(f"O maior valor foi {max(tupla)}")


