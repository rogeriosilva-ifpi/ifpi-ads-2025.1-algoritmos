def recebe_numero_decimal():
    numero_decimal = float(input("Digite um número decimal: "))
    return numero_decimal


def recebe_numero_decimal_positivo():
    numero_decimal_positivo = float(input("Digite um número decimal positivo!: "))
    
    if numero_decimal_positivo < 0:
        return recebe_numero_decimal_positivo()
    
    return numero_decimal_positivo

valor_minimo = 7.35
valor_maximo = 24.15

def recebe_numero_decimal_com_valor_minimo(valor_minimo):
    numero_decimal_com_valor_minimo = float(input("Digite um número que seja no minimo 7.35!: "))
    
    if numero_decimal_com_valor_minimo < valor_minimo:
        return recebe_numero_decimal_com_valor_minimo(valor_minimo)
    
    return numero_decimal_com_valor_minimo


def recebe_numero_decimal_com_valor_maximo(valor_maximo):
    numero_decimal_com_valor_maximo = float(input("Digite um número que seja no maximo 24.15!: "))
    
    if numero_decimal_com_valor_maximo > valor_maximo:
        return recebe_numero_decimal_com_valor_maximo(valor_maximo)
    
    return numero_decimal_com_valor_maximo

def recebe_numero_decimal_no_intervalo(valor_minimo, valor_maximo):
    numero_decimal = float(input("Digite um número decimal entre 7.35 e 24.15!: "))
    
    if numero_decimal < valor_minimo:
        return recebe_numero_decimal_no_intervalo(valor_minimo, valor_maximo)
    elif numero_decimal > valor_maximo:
        return recebe_numero_decimal_no_intervalo(valor_minimo, valor_maximo)
    return numero_decimal



recebe_numero_decimal()
recebe_numero_decimal_positivo()
recebe_numero_decimal_com_valor_minimo(valor_minimo)
recebe_numero_decimal_com_valor_maximo(valor_maximo)
recebe_numero_decimal_no_intervalo(valor_minimo, valor_maximo)