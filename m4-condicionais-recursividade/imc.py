from io_utils import obter_numero_real


def main():
  altura = obter_numero_real('Altura (m): ')
  peso = obter_numero_real('Peso (kg): ')

  imc = calcular_imc(peso, altura)

  classificacao = classificar_imc(imc)

  print(f'Seu IMC é {imc:.1f}, você está "{classificacao}"')


def calcular_imc(peso: float, altura: float):
  return peso / (altura**2)


def classificar_imc(imc: float):
  if imc < 18.5:
    return 'Abaixo do Peso'
  elif imc <= 24.9:
    return 'Peso Normal'
  elif imc <= 29.9:
    return 'Sobrepeso'
  elif imc <= 34.9:
    return 'Obesidade Grau I'
  elif imc <= 39.9:
    return 'Obesidade Grau II'
  else:
    return 'Obesidade Grau III'

main()