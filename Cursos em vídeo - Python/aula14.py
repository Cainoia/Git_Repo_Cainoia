c = 1 # precisa começar o valor c

# Utilizar quando você sabe ou não sabe o limite, o for você precisa sabe o limite

# while c < 10:           
#     print(c)
#     c += 1      # c = c + 1
# print("Fim")

# while c != 0:
#     c = int(input("Digite uma valor: "))

# Quantos números eram pares e quantos números era ímpares:

i = 1

impar = 0

par = 0

# par = impar = 0

while i != 0:
    
    i = int(input("Digite um número: "))

    if i != 0:

        if i % 2 == 0:

            par = par + 1 # par += 1

        else:

            impar += 1


print("Fim")
print(f"A quantidade de números pares foi: {par}")
print(f"A quantidade de números impares foi: {impar}")
