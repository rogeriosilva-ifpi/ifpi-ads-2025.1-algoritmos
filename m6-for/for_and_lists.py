from math import sqrt


def main():
  frutas = ['Manga', 'Melancia', 'Banana', 'Uva', 'Morango', 'Pitomba']

  frutas.append('Kiwi')

  for fruta in frutas:
    if not eh_primo(len(fruta)):
      print(f'A fruta {fruta} tem {len(fruta)} letras')
  
  print('Fim.')


def eh_primo(n: int) -> bool:
  limite = int(sqrt(n))
  contador = 0

  for i in range(1, limite+1, 1):
    if n % i == 0:
      contador += 1
  
  return contador == 1



main()