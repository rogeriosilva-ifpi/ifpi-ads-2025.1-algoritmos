from io_utils import obter_numero_real


def principal():
  peso = obter_numero_real('Peso (kg): ')
  altura = obter_numero_real('Altura (m): ')

  imc = calcular_imc(peso, altura)

  print(f'Seu IMC é {imc:.2f}')


def calcular_imc(peso, altura):
  imc = peso / (altura*altura)
  return imc

principal()