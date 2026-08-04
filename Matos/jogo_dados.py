import random

def jogada(nome):

    valor_jogada = random.randint(1,6)

    tupla = (nome, valor_jogada)

    return tupla

def soma_pontos(lista_tuplas): 

    dicicionario = {}

    for tupla in lista_tuplas:
        if tupla[0] in dicicionario:
            dicicionario[tupla[0]] += tupla[1]
        elif tupla[0] not in dicicionario:
            dicicionario[tupla[0]] = tupla[1]

    return dicicionario

def vencedor(dicionario):

    nome_ganhador = ""

    maior_resultado = max(dicionario.values())

    for nome, resultado in dicionario.items():

        if resultado == maior_resultado:

            nome_ganhador = nome

#    print(maior_resultado)
#
#    for nome, resultado in dicionario.items():
#
#        if resultado > resultado_ganhador:
#
#            resultado_ganhador = resultado
#
#            nome_ganhador = nome
#
    tupla = (nome_ganhador, maior_resultado)

    return tupla

