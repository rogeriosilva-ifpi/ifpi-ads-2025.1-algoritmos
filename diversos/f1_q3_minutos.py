# 3. Leia um valor em minutos, calcule e 
# escreva o equivalente em horas e minutos.

# Entrada
minutos = int(input('Minutos: '))

# Processamento
horas = minutos // 60
minutos_rest = minutos % 60

# Saída (f-string / interpolacao de string)
print(f'> {minutos}min equivalem a {horas}h{minutos_rest}min')