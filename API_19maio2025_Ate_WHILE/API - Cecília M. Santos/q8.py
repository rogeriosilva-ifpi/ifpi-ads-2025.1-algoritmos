def main():
    limite_n = int(input('Limite N inferior: '))
    limite_m = int(input('Limite M inferior: '))

    diz_se_numero_eh_perfeito(limite_n, limite_m)


def diz_se_numero_eh_perfeito(n, m):
    numero = n

    while numero <= m:
        resposta = calcula_divisores(numero)
        print(f'{numero} - {resposta}')

        numero += 1


def calcula_divisores(n):
    pretendente = 0
    soma = 0

    while pretendente < n:
        pretendente += 1
        if n % pretendente == 0:
            soma += pretendente
        else:
            continue
        
        if soma == n:
            return 'É perfeito'
        else:
            return 'Não é perfeito'


main()