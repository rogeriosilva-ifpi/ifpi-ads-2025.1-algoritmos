#entrada
nota1 = float(input('Digite a nota 1:'))
nota2 = float(input('Digite a nota 2:'))
nota3 = float(input('Digite a nota 3:'))
peso1 = int(input('Digite o peso 1:'))
peso2 = int(input('Digite o peso 2:'))
peso3 = int(input('Digite o peso 3:'))

#processamento
media_ponderada = (nota1*peso1 + nota2*peso2 + nota3*peso3) / (peso1+peso2+peso3)
#saida
print(f'A média ponderada das notas: {media_ponderada:.2f}') 