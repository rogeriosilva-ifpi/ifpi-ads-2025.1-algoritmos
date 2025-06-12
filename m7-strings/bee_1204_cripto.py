from str_utils import is_letter

def main():
  qtd = int(input())
  
  for _ in range(0, qtd, 1):
    texto = input()

    etapa_1 = deslocar_letras(texto)
    etapa_2 = inverter_texto2(etapa_1)
    etapa_3 = deslocar_texto_parte_final(etapa_2)
    print(etapa_3)


def deslocar_letras(texto):
  novo_texto = ''
  
  for caracter in texto:
    if is_letter(caracter):
      novo_texto += chr(ord(caracter) + 3)
    else:
      novo_texto += caracter
  
  return novo_texto


def inverter_texto(texto):
  novo_texto = ''

  for caracter in texto:
    novo_texto = caracter + novo_texto
  
  return novo_texto


def inverter_texto2(texto):
  novo_texto = ''

  for i in range(len(texto)-1, -1, -1):
    novo_texto += texto[i]
  
  return novo_texto

def deslocar_texto_parte_final(texto):
  meio = len(texto) // 2

  novo_texto = ''
  for index in range(0, len(texto), 1):
    caracter_atual = texto[index]
    if index >= meio:
      novo_texto += chr(ord(caracter_atual) - 1)
    else:
      novo_texto += caracter_atual
  
  return novo_texto





main()