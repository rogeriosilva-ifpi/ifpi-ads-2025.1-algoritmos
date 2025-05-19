

def recebe_numero_inteiro():
    numero_inteiro = int(input("Digite um número inteiro: "))
    return numero_inteiro


def recebe_numero_inteiro_positivo():
    numero_inteiro_positivo = int(input("Digite um número inteiro positivo!: "))
    
    if numero_inteiro_positivo < 0:
        return recebe_numero_inteiro_positivo()
    
    return numero_inteiro_positivo

valor_minimo = 8
valor_maximo = 24

def recebe_numero_inteiro_com_valor_minimo(valor_minimo):
    numero_inteiro_com_valor_minimo = int(input("Digite um número que seja no minimo 8!: "))
    
    if numero_inteiro_com_valor_minimo < valor_minimo:
        return recebe_numero_inteiro_com_valor_minimo(valor_minimo)
    
    return numero_inteiro_com_valor_minimo


def recebe_numero_inteiro_com_valor_maximo(valor_maximo):
    numero_inteiro_com_valor_maximo = int(input("Digite um número que seja no maximo 24!: "))
    
    if numero_inteiro_com_valor_maximo > valor_maximo:
        return recebe_numero_inteiro_com_valor_maximo(valor_maximo)
    
    return numero_inteiro_com_valor_maximo

def recebe_numero_inteiro_no_intervalo(valor_minimo, valor_maximo):
    numero_inteiro = int(input("Digite um número inteiro entre 8 e 24!: "))
    
    if numero_inteiro < valor_minimo:
        return recebe_numero_inteiro_no_intervalo(valor_minimo, valor_maximo)
    elif numero_inteiro > valor_maximo:
        return recebe_numero_inteiro_no_intervalo(valor_minimo, valor_maximo)
    
    return numero_inteiro



recebe_numero_inteiro()
recebe_numero_inteiro_positivo()
recebe_numero_inteiro_com_valor_minimo(valor_minimo)
recebe_numero_inteiro_com_valor_maximo(valor_maximo)
recebe_numero_inteiro_no_intervalo(valor_minimo, valor_maximo)