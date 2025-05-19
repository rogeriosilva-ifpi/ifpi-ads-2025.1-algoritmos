def receber_num_int(label):
    entrada = input(label)

    try:
        num = int(entrada)
        return num
    except:
        print(f'"{entrada}" não é um inteiro válido. Tente novamente!')
        return receber_num_int(label)


def receber_int_positivo(label):
    entrada = receber_num_int(label)

    if entrada >= 0:
        return entrada
    else:
        print(
            f'O número digitado "{entrada}" não é um inteiro positivo. Tente novamente!')
        return receber_num_int(label)


def receber_int_min(label, limite):
    entrada = receber_num_int(label)

    if entrada >= limite:
        return entrada
    else:
        print(f'O número "{entrada}" está abaixo do limite. Tente novamente!')
        return receber_int_min(label, limite)


def receber_int_max(label, limite):
    entrada = receber_num_int(label)

    if entrada <= limite:
        return entrada
    else:
        print(f'O número "{entrada}" está acima do limite. Tente novamente!')
        return receber_int_max(label, limite)


def receber_int_in_faixa(label, limit_min, limit_max):
    entrada = receber_num_int(label)

    if entrada >= limit_min and entrada <= limit_max:
        return entrada
    else:
        print(f'O número "{entrada}" não está no limite estabelecido [{limit_min}, {limit_max}]')
        return receber_int_in_faixa(label, limit_min, limit_max)
