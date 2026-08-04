# for i in range(0, 7, 2):      # o terceiro número é o passo
#     print(i)


# i = int(input("Início: "))
# f = int(input("Fim: "))
# p = int(input("Passo: "))
# for c in range(i, f + 1, p):
#   print(c)

# Contagem regressiva de 10 a 0

import time

def contagem_regessiva():

    for i in range(10, -1, -1):
        print(i)
        time.sleep(1)

contagem_regessiva()


