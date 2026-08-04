def notas():

    lista = []

    for i in range(2):
        valor = float(input(f"Digite o valor da {i + 1}ª nota: "))
        lista.append(valor)

    media = (lista[0] + lista[1]) / 2

    if media < 5.0:
        print(f"Nota final: {media}\n\033[4mReprovado!!")
    
    elif media > 5.0 and media < 6.9:
        print(f"Nota final: {media}\n\033[4mRecuperação!!")

    else: 
        print(f"Nota final: {media}\n\033[4mAprovado!!")

notas()