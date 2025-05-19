from q2_int_utils import obter_numero_inteiro_min
from math import sqrt


def main():
    n = obter_numero_inteiro_min('Limite Inferior: ', 1)
    m = obter_numero_inteiro_min('Limite Superior: ', n + 1)

    while n <= m:
        print(f'{n} - {eh_primo(n)}')
        n += 1


def eh_primo(n: int):
    raiz = sqrt(n)
    contador = 2
    divisores = 0

    while contador <= raiz:
        if raiz % contador == 0:
            divisores += 1
        contador += 1

    if n == 1:
        return 'não é primo'
    if 0 < divisores < 2:
        return 'é primo'
    else:
        return 'não é primo'


main()