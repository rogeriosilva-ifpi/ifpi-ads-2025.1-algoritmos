def receber_numero_inteiro():
    valor = int(input("Digite um número inteiro: "))
    return valor

def receber_numero_inteiro_positivo():
    valor = int(input("Digite um número inteiro: "))
    if valor >= 1:
        return valor
    
def receber_numero_inteiro_minimo():
    valor = int(input("Digite um número inteiro: "))
    if valor >= 1:
        return min(valor)

def receber_numero_inteiro_maximo():
    valor = int(input("Digite um número inteiro: "))
    if valor >= 1:
        return max(valor)

def receber_numero_inteiro_faixaXY():
    valor = int(input("Digite um número inteiro: "))
    if valor >= 1:
        return min(valor) and max(valor)