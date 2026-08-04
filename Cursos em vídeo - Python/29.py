def velocidade_carro():

    for i in range(1):
        x = int(input("Qual a velocidade atual do carro?"))

    if x < 80:
        print("Tenha um bom dia! Dirija com segurança!")
    else:
        multa = (x - 80) * 7
        print(f"MULTADO! Você excedeu o limite permitido que é de 80 km/h\nVocê deve pagar uma multa de R$ {multa}!")
        print("Tenha um bom dia! Dirija com segurança!")

velocidade_carro()