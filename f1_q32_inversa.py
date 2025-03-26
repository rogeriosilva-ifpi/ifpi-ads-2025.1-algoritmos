# 32. Leia um número inteiro (3 dígitos), 
# calcule e escreva a diferença entre o número e seu inverso.

# entrada
numero = int(input('Número: '))

# processador
centena = numero // 100
dezena = (numero % 100) // 10
unidade = (numero % 100) % 10 

inverso = (unidade * 100) + (dezena * 10) + centena

diferenca = numero - inverso 

#saida

print(f"{numero} - {inverso} = {diferenca}")