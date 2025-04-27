def main():
  nota1 = float(input('Insira a primeira nota: '))
  nota2 = float(input('Insira a primeira nota: '))
  nota3 = float(input('Insira a primeira nota: '))

  media = calcular_media(nota1, nota2, nota3)

  print(f'Sua média foi {media:0.1f}')

  if nota1 == 0.0 or nota2 == 0.0 or nota3 == 0.0 or media < 5:
    print('Reprovado')
  elif media < 7.0:
    print('Recuperação')
  else: 
    print('Aprovado')

  

def calcular_media(nota1, nota2, nota3):
  return (nota1 + nota2 + nota3) / 3

main()