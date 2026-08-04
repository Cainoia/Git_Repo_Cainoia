# É interessante eu dar uma olhada depois para freezar esses conceitos, não fiz com dicionário

def numero_inteiro():

    lista_numero = []

    lista_conversao = ["binário", "octal", "hexadecimal"]

    for i in range(1):
        numero = int(input("Digite um número: "))
        lista_numero.append(numero)

    print(f"Bases possíveis de conversão: {lista_conversao}")

    x = str(input("Digite a base de conversão desejada: "))

    if x == lista_conversao[0]:
        y = bin(lista_numero[0])[2:]

    elif x == lista_conversao[1]:
        y = oct(lista_numero[0])[2:]

    elif x == lista_conversao[2]:
        y = hex(lista_numero[0])[2:]

    else:
        print("Não foi possível fazer a base de conversão")

    print(f"O numero {numero} foi definido com a base {x} e teve como resultado {y}")

    
numero_inteiro()