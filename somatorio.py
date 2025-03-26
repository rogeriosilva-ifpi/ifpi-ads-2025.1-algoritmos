print('Hello ADS 2025.1')
print('--------------------')
print('>>>>> Soma de N até M <<<<')

# entrada
limite_inferior = int(input('Limite Inferior: '))
limite_superior = int(input('Limite Superior: '))

# processamento
soma_par = limite_inferior + limite_superior

quantidade_pares = (limite_superior - limite_inferior + 1) / 2

somatorio = soma_par * quantidade_pares

# saída
print(somatorio)