

# interessante o exercício, não peguei direito a ideia do somatório ainda mas gostei

def mult_impar():

    s = 0           # inicializa o somatório, fica porque porque ele não pode resetar

    contador = 0

    for i in range(1,501): # ou (1, 501, 2) sem o if de impar ou (1 , 501, 6) sem os if's

        if i % 2 != 0 and i % 3 == 0:
            
            s += i  # soma i ao acumulador que é igual ao s = s + i

            contador += 1  

            print(i, end="+")
            print(contador)

    return s, contador

teste = mult_impar()


print(teste)
