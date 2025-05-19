def utils_float():
    def receber_numero_decimal():
        num = float(input('Digite um número decimal: '))

    receber_numero_decimal()

    def receber_numero_decimal_positivo():
        num = float(input('Digite um número decimal positivo: '))

    receber_numero_decimal_positivo()

    def receber_numero_decimal_minimo():
        minimo = float(input('Digite o valor minímo: '))
        receber_numero_decimal()
        while receber_numero_decimal < minimo:
            print('O valor é menor que o valor minímo. Digite o número novamente.')
            break 
        receber_numero_decimal()

    receber_numero_decimal_minimo()

    def receber_numero_decimal_máximo():
        maximo = float(input('Digite o valor máximo: '))
        receber_numero_decimal()
        while receber_numero_decimal > maximo:
            print('O valor é maior que o valor máximo. Digite o número novamente.')
            break 
        receber_numero_decimal()

    receber_numero_decimal_máximo()

    def receber_numero_em_faixa_max_min():
        minimo = float(input('Digite o valor mínimo: '))
        maximo = float(input('Digite o valor máximo: '))
        receber_numero_decimal()
        while receber_numero_decimal > maximo and receber_numero_decimal < minimo:
           print('O valor não está na faixa informada. Digite o número novamente.')
           break         
        receber_numero_decimal()
           


utils_float()    