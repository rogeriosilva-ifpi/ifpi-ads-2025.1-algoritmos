def main():
    limite_n = int(input('Limite N: '))
    limite_m = int(input('Limite M: '))

    numero = limite_n

    while numero <= limite_m:
        resposta, qntd_divisores = verifica_se_eh_primo(numero)
        print(f'{numero} - {resposta}')
        if resposta == 'Não é primo':
              print(f'Qntd de divisores: {qntd_divisores}')

        numero += 1


def verifica_se_eh_primo(n):
    qntd_divisores = 0
    raiz = n ** 0.5
    pretendente = raiz // 1

    while pretendente > 0:
        if n % pretendente == 0:
                qntd_divisores += 1
                divisores_total = qntd_divisores + 1   # contando o número 1
        pretendente -= 1

    if divisores_total == 2:
            return 'É primo', divisores_total
    elif divisores_total != 2:
            return 'Não é primo', divisores_total


main()