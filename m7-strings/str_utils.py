def avoids(palavra, letras_proibidas):
  for letra in palavra:
    if contem_caracter(letras_proibidas, letra):
      return False
  
  return True


def contem_caracter(palavra, caracter):
  for letra in palavra:
    if letra == caracter:
      return True
  

  return False

def uses_only(palavra,letras_permitidas):
  for letra in palavra:
    if not contem_caracter(letras_permitidas,letra):
      return False
  
  return True

def uses_all(palavra, letras_obrigatorias):
  for letra in letras_obrigatorias:
    if not contem_caracter(palavra, letra):
      return False
  
  return True


def is_abecedarian(word):
  anterior = word[0]

  for i in range(1, len(word)):
    atual = word[i]
    if anterior > atual:
      return False
    
    anterior = atual
  
  return True


def to_lower(text):
  new_text = ''
  for char in text:
    if is_upper_letter(char):
      code = ord(char)
      new_code = code + 32
      lower_char = chr(new_code)
      new_text += lower_char
    else:
      new_text += char

  return new_text


def is_upper_letter(char):
  return ord(char) >= 65 and ord(char) <= 90
