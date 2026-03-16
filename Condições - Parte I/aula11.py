# Cores no terminal

# Código ANSI para cores

#\033[style; text; background m = cor de estilo, cor de fonte, cor de fundo

#\033[0;33;44m

# style 0 1 4 7 ; None Negrito Sublinhado Inverter

# text 30 31 32 33 34 35 36 37 ; Branco Vermelho Verde Amarelo Azul Magenta Ciano Cinza

# background 40 41 42 43 44 45 46 47 ; Branco Vermelho Verde Amarelo Azul Magenta Ciano Cinza

print('\033[1;35;47molá mundo\033[m')

x = "feliz"

print(f"Olá mundo {"\033[1;35;45m"}{x}{"\033[m"}!!!")

y = 'curso de python no cursoemvideo'
print(f"{y[1:5]}")


