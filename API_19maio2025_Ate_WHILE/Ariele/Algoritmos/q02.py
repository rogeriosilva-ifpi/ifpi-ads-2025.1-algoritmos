def main():
    inteiro = receber_inteiro("Inteiro: ")
    inteiro_positivo = receber_inteiro_positivo('Inteiro Positivo: ')
    inteiro_minimo= receber_inteiro_minimo('Inteiro Minimo: ', 100)
    receber_max = receber_inteiro_max('Inteiro Maximo: ', 100)
    min_max = receber_inteiro_min_max ('Inteiro: ', 100, 1000)
   
def receber_inteiro(label: str):
  entrada = input(label)
  
  try:
      numero = int(entrada)
      return numero
  except ValueError:
      print('Por favor digite um número inteiro.')
      return receber_inteiro(label)


def receber_inteiro_positivo(label: str):
  entrada = input(label)
  
  try:
      numero = int(entrada)
      if numero < 0:
          print('Digite um número inteiro positivo')
          receber_inteiro_positivo(label)
      return numero
  except ValueError:
      print('Por favor digite um número inteiro.')
      return receber_inteiro(label)
  

def receber_inteiro_minimo(label: str, min_value:int):
  entrada = input(label)
  try:
      numero = int(entrada)
      if numero < min_value:
          print(f'Digite um número acima de {min_value}')
          receber_inteiro_minimo(label, min_value)
      return numero
  except ValueError:
      print('Por favor digite um número inteiro.')
      return receber_inteiro_minimo(label)
  
  
def receber_inteiro_max(label: str, max_value:int):
  entrada = input(label)
  try:
      numero = int(entrada)
      if numero > max_value:
          print(f'Digite um número abaixo de {max_value}')
          receber_inteiro_max(label, max_value)
      return numero
  except ValueError:
      print('Por favor digite um número inteiro.')
      return receber_inteiro_max(label)
  
  
  
def receber_inteiro_min_max(label: str, min_value:int, max_value: int): 
    entrada = input(label)
    try:
      numero = int(entrada)
      if numero > max_value:
          print(f'Digite um número abaixo de {max_value}')
          return receber_inteiro_min_max(label,max_value,min_value)
      if numero < min_value:
          print(f'Digite um número acima de {min_value}')
          return receber_inteiro_min_max(label, max_value,min_value)
      return numero
    except ValueError:
      print('Por favor digite um número inteiro.')
      return receber_inteiro_min_max(label,max_value,min_value)

main()