def receber_numero_inteiro(a):
    numero = int(input('Digite um número inteiro: '))

receber_numero_inteiro()


def receber_numero_inteiro_positivo():
    num = int(input('Digite um número inteiro positivo: '))

receber_numero_inteiro_positivo()


def receber_numero_inteiro_minimo():
    minimo = int(input('Digite o valor minímo: '))
    receber_numero_inteiro()
    while receber_numero_inteiro < minimo:
        print('O valor é menor que o valor minímo. Digite o número novamente.')
        break 
    receber_numero_inteiro()

receber_numero_inteiro_minimo()


def receber_numero_inteiro_máximo():
    maximo = int(input('Digite o valor máximo: '))
    receber_numero_inteiro()
    while receber_numero_inteiro > maximo:
        print('O valor é maior que o valor máximo. Digite o número novamente.')
        break 
    receber_numero_inteiro()

receber_numero_inteiro_máximo()


def receber_numero_em_faixa_max_min():
    minimo = int(input('Digite o valor mínimo: '))
    maximo = int(input('Digite o valor máximo: '))
    receber_numero_inteiro()
    while receber_numero_inteiro > maximo and receber_numero_inteiro < minimo:
        print('O valor não está na faixa informada. Digite o número novamente.')
        break         
receber_numero_inteiro()
           