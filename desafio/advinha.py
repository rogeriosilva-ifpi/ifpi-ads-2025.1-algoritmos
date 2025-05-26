import random

def main():
  numero = random.randint(1,100)
  tentativas = 10
  pontos = 0

  while tentativas > 0:
    tentativas -= 1
    palpite = int(input("Palpite: "))
    
    if palpite == numero:
      pontos = tentativas * 10
      print("Você acertou!!!")
      print(f"Pontuação: {pontos} pontos")
      break
    elif palpite > numero:
      print("Tente novamente com um número menor")
    else:
      print("Tente novamente com um número maior")

  if tentativas == 0:
    print("Muito ruim filho kkkkkkk")


main()