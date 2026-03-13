def aumento_salario():

    salario = []

    for i in range(1):
        valor = int(input(f"Digite o valor do seu salário: "))
        salario.append(valor)

    if salario[0] > 1250:
        aumento = salario[0] * 0.1
    else:
        aumento = salario[0] * 0.15

    print(f"O aumento do seu salário será de R$ {aumento}")

aumento_salario()
