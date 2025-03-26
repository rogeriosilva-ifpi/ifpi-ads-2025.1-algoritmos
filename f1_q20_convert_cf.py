# 20. Leia uma temperatura em °C, 
# calcule e escreva a equivalente em °F. 
# (t°F = (9 * t°C + 160) / 5)

# Entrada
temperatura_c = int(input('Temperatura (C): '))

# Processamento
temperatura_f = (9 * temperatura_c + 160) / 5

# Saída
resultado = f'Temperatura: {temperatura_c}C equivalem a {temperatura_f}F'
print(resultado)