def numero_inteiro():

    lista_conversao = ["binário", "octal", "hexadecimal"]

    x = int(input("Digite um número: "))

    print("Bases possíveis para conversão: ")           # Não entendi direito como fazer isso
    for i, base in enumerate(lista_conversao):          # nesse caso está servindo como uma tabelhinha
        print(f"[{i+1}] {base}")

    opcao = int(input("Escolha o valor (1, 2 ou 3) para a conversão desejada: "))

    if opcao == 1:
        y = bin(x)[2:]
        print(f"O resultado do número {x} foi {y} em base {lista_conversao[0]}")
    
    elif opcao == 2:
        y = oct(x)[2:]
        print(f"O resultado do número {x} foi {y} em base {lista_conversao[1]}")
    
    elif opcao == 3:
        y = hex(x)[2:]
        print(f"O resultado do número {x} foi {y} em base {lista_conversao[2]}")
    
    else:
        print("\033[4mNão foi possível achar a solução!!\033[m")
    

numero_inteiro()