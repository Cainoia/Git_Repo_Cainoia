# Interessante ver depois para firmar conceitos de lista

# () = tupla       => imutável
# [] = Lista       => mutável
# {} = Dicionário  => 

# função .extend() => lista = [1,2] => lista.append([3,4]) => lista = [1,2,[3,4]] 
# função .extend() => lista = [1,2] => lista.extend([3,4]) => lista = [1,2,3,4] 

def comprar_casa():

    valores = []

    for i in range(1):
        valor_casa = float(input("Qual o valor da casa? "))
        valor_salario = float(input("Qual o seu sálario? "))
        anos = float(input("Em quantos anos pretende pagar? "))
        #valores.append((valor_casa, valor_salario, anos)) # colocar os parêntes para adicionar como uma tupla
        valores.append([valor_casa, valor_salario, anos]) # colocar os parêntes para adicionar como uma lista
        #valores.extend([valor_casa, valor_salario, anos]) # Adiciona como elementos separados

    #for i in range(1):                                    # Utilizar dicionários dentro de uma lista 
        #dados = {"valor casa": float(input("Qual o valor da casa? ")),
        #"valor_salario" : float(input("Qual o seu sálario? "))
        #"anos" : float(input("Em quantos anos pretende pagar? "))
        #}
        #valores.append(dados)
    
    prestacao = valores[0][0] / ( valores[0][2] * 12 )

    print(f"O valor da prestação é de R$ {prestacao} durante {valores[0][2] * 12} meses")

    if prestacao >= valores[0][1] * 0.3:
        print(f"Com seu salário de R$ {valores[0][1]}, você não consegue pagar a pretação de R$ {prestacao}\nSeu empréstimo foi negado !!")
    else:
        print("\033[4;35mParabens!!\033[m Seu empréstimo foi aprovado")


comprar_casa()
    