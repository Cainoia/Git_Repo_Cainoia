# Utilizando apenas lógica

def maior_menor():

    x = int(input(f"Digite um numero:"))
    y = int(input(f"Digite um numero:"))
    z = int(input(f"Digite um numero:"))

    maior = x
    menor = x

    if y > x and y > z:
        maior = y
    if z > x and z > y:
        maior = z
    
    if y < x and y < z:
        menor = y
    if z < x and z < y:
        menor = z
    

    print(f"Os numeros digitados foram {x, y, z}")
    print(f"O menor valor é {menor}")
    print(f"O maior valor é {maior}")

maior_menor()