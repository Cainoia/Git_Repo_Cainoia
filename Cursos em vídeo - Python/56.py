
def usuario():

    age = 0
    maioria_homem = 0
    nome_velho = ""
    mulher_nova = 0

    for i in range(0,4):

        print(f"===== {i + 1}ª Pessoa =====")

        nome = str(input("Nome: ")).strip()

        idade = int(input("Idade: "))

        sexo = str(input("Sexo [M/F]: ")).lower().strip()
                
        age += idade      # age = age + idade

        if i == 0 and sexo in "Mm":

            maioria_homem = idade
            nome_velho = nome

        if sexo in "Mm" and idade > maioria_homem:

            maioria_homem = idade
            nome_velho = nome

        if sexo in "Ff" and idade < 20:

            mulher_nova += 1


    
    media = age / i

    print(f"A média das idade foi = {media:2f}")
    print(f"O nome do homem mais velho = {nome_velho} com idade = {maioria_homem}")
    print(f"A quantidade de mulheres com menos de 20 anos = {mulher_nova}")


usuario()
    