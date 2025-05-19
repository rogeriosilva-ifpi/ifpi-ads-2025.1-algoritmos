from q2_int_utils import obter_numero_inteiro_min


def main():
    limite_inferior = obter_numero_inteiro_min('Limite Inferior: ', 1)
    limite_superior = obter_numero_inteiro_min('Limite Superior: ', limite_inferior + 1)

    contador = 1
    while limite_inferior <= limite_superior:
        if limite_inferior % contador == 0:
            print(f'{limite_inferior} - {eh_perfeito(limite_inferior)}')
        limite_inferior += 1


def eh_perfeito(numero: int):
    contador = 1
    soma = 0
    while contador < numero:
        if numero % contador == 0:
            soma += contador

        contador += 1

    if soma == numero :
        return 'é perfeito'
    else:
        return 'não é perfeito'


main()