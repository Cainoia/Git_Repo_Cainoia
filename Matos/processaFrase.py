def dict_letras(frase):

    frase_separada = list(frase)

    dicionario = {}

    for caracter in frase_separada:

        if caracter in dicionario:

            dicionario[caracter] += 1

        elif caracter not in dicionario:

            dicionario[caracter] = 1

    # print(frase_separada)

    return dicionario

def inverte_dict(dicionario):

    dicionario_invertido = {}

    for letra, numero in dicionario.items():

        if numero not in dicionario_invertido:

            dicionario_invertido[numero] = list(letra)

        else:

            dicionario_invertido[numero] += letra
            dicionario_invertido[numero] = list(dicionario_invertido[numero])

        # print(type(dicionario_invertido[numero]))

    print(dicionario_invertido)
    return dicionario_invertido

def tam_rep(dicionario):

    maior_valor = max(dicionario.keys())

    print(maior_valor)

    quantidade = len(dicionario[maior_valor])

    print(quantidade)

    return maior_valor, quantidade


x = 'aaaa bbb hdhdj kkkkl kdk'

a = dict_letras(x)

b = inverte_dict(a)

print(tam_rep(b))

