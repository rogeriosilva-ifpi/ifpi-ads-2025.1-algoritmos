def main():
    nome = get_text('Digite o nome de usuário: ')

    if len(nome) % 2 != 0:
        contador = 1
        while contador <= len(nome):
          if len(nome) % contador == 0:
            print(f'{contador}')
          contador += 1
    else:
       contador = len(nome)
       while contador > 0:
          if len(nome)/contador == 0:
            print(f'{contador}')
          contador -= 1
       


def get_text(label: str):
  return str(input(label))

def get_text_min(label: str, min_value: int):
  text = get_text(label)
   
  while len(text) < min_value:
    print(f'O valor do texto deve ter no mínimo {min_value} caracteres')
    text  = get_text(label)
  return text

main()