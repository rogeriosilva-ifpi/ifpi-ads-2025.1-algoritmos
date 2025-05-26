def main():
    numero_1 = int(input('Número 1: '))
    numero_2 = int(input('Número 2: '))

    calcula_mdc(numero_1, numero_2)


def calcula_mdc(n_1, n_2):
    maior = max(n_1, n_2)
    menor = min(n_1, n_2)
    anterior = maior
    sucessor = menor
    subtracao == 0

    if subtracao == 0:
        mdc = menor
    else:
        while True:
            subtracao = anterior - sucessor
            sucessor = anterior
            subtracao = sucessor

            if subtracao == 0:
                mdc = subtracao
                break
            
    # faltou retornar
    print(F'O MDC de {maior} e {menor} é {mdc}')


main()
        
        
                


            

