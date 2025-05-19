from q2_int_utils import receber_num_int


def num_eh_perfeito():
    N = receber_num_int('digite o limite minino: ')
    M = receber_num_int('digite o limite maximo: ')

    numero = N
    while numero >= N and numero <= M:
        contador=1
        somatorio=0
        while contador < N:
            if N % contador == 0:
                somatorio += contador
                contador += 1
            else:
                contador += 1
        if somatorio == N:
            print('Somatorio:', somatorio, 'Numero é perfeito')
        else:
            print('Somatorio:', somatorio)
        
        numero += 1


num_eh_perfeito()
