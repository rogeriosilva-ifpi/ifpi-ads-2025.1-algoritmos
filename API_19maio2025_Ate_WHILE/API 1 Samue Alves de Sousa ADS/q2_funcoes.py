def receber_inteiro():
    inteiro = int(input('Digite um valor inteiro: '))
    
    if inteiro > 0:
        return inteiro


def receber_positivo():
    int_posi = int('Digite um valor inteiro positivo: ')
    try:
        if int_posi > 0 :
            return int_posi
    
    except:
        return int_posi


def receber_int_min():
    valor = int(input('Digite um valor maior que 5'))
    if valor < 5:
        print('numero invalido, o numero precisar ser pelo menos 5')
    elif valor >= 5:
        return('Valor correto')


def receber_int_max():
    valor_max = int(input('Digite um valor até 20: '))
    if valor_max > 20:
        print('O valor maximo é 20')
    elif valor_max <= 20:
        return valor_max


def receber_int_mx_my():
    valor_faixa = int(input('Digite um valor entre 1 e 50: '))
    if valor_faixa < 1 and valor_faixa > 50:
        print('Valores estao na faixa errada')
    elif valor_faixa >= 1 and valor_faixa <= 50:
        print('Valores corretos')
