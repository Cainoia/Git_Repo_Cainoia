times = ("Palmeiras", "Flamengo", "Athletico-PR", "Fluminense", "Bahia", "Bragantino", "Cruzeiro", "Botafogo"
         , "Coritinhas", "Atlético-MG", "Coritiba", "São Paulo", "Vitória", "Mirassol", "Santos", "Internacional"
         , "Grêmio", "Vasco", "Remo", "Chapecoense")

primeiros_5 = times[:5]

print(f"Os primeiros 5 colocados são {primeiros_5}")

ultimos_4 = times[-4:]

print(f"Os ultimos 4 são {ultimos_4}")

print("="*30)

lista_alfa = sorted(list(times))

for i, base in enumerate(lista_alfa):

    print(f"{i+1}º -> {base}")

print("="*30)

for i in range(0, len(times)):

    if times[i] == "Chapecoense":

        print(f"O time {times[i]} está na {i+1}ª posição")