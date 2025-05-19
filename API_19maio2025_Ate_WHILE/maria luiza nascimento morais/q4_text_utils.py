def get_text(label: str):
  return str(input(label))

def get_text_min(label: str, min_value: int):
  text = get_text(label)
   
  while len(text) < min_value:
    print(f'O valor do texto deve ter no mínimo {min_value} caracteres')
    text  = get_text(label)
  return text

def get_text_max(label: str, max_value: int):
  text = get_text(label)
   
  while len(text) > max_value:
    print(f'O valor do texto deve ter no máximo {max_value} caracteres')
    text  = get_text(label)
  return text

def get_text_in_range(label: str, min_value: int, max_value: int):
  text = get_text(label)

  while len(text) > max_value or len(text) < min_value:
    print(f'Valor de caracteres fora da faixa ({min_value}-{max_value})')
    text = get_text(label)
  return text