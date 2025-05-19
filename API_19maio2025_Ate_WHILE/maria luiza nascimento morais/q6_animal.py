def main():
  get_text_min('Digite o nome de um animal: ', 7)
    






def get_text(label: str):
  return str(input(label))

def get_text_min(label: str, min_value: int):
  text = get_text(label)
   
  while len(text) < min_value:
    print(f'O valor do texto deve ter no mínimo {min_value} caracteres')
    text  = get_text(label)
  return text