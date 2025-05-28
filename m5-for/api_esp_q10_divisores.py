def main():
  a = get_int('A: ')
  b = get_int_min('B: ', a+11)

  for number in range(a, b+1, 1):
    qtd = count_divs(number)
    is_prime = qtd == 2
    print(f'>Number: {number} - (divs: {qtd}) - Is it prime?: {is_prime}')

# utils...
def get_int(text: str):
  value = input(text)

  try:
    number = int(value)
    return number
  except ValueError:
    print(f'O valor "{value}" não é um inteiro válido!')
    return get_int(text)
  

def get_int_min(text: str, min: int):
  number = get_int(text)

  while number < min:
    print('Valor incorreto!')
    print(f'O número "{number}" é menor que o mínimo: {min}.')
    number = get_int(text)

  return number


def count_divs(number: int):
  count = 0
  for d in range(1, number+1, 1):
    if number % d == 0:
      count += 1
  
  return count

main()
