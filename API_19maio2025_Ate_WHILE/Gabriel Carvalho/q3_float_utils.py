def main():

    def receber_decimal():
        while True:
            try:
                valor = float(input('Digite um número decimal: '))
                return valor
            except ValueError:
                print('Valor inválido. Digite um número decimal')

    def receber_decimal_positivo():
        while True:
            try:
                valor = float(input('Digite um número decimal positivo: '))
                if valor > 0:
                    return valor 
                else:
                    print('O valor deve ser positivo')
            except ValueError:
                print('Valor inválido, por favor digite um número decimal positivo')

    def receber_decimal_minimo(minimo):
        while True:
            try:
                valor = float(input(f'Digite um número decimal maior ou igual a {minimo}'))
                if valor >= minimo:
                    return valor
                else:
                    print(f'O número deve ser maior ou igual a {minimo}')
            except ValueError:
                print(f'Valor inválido, insira um número maior ou igual a {minimo}')

    def receber_decimal_maximo(maximo):
        while True:
            try:
                valor = float(input(f'Digite um número decimal menor ou igual a {maximo}'))
                if valor <= maximo:
                    return valor
                else:
                    print(f'O número deve ser menor ou igual a {maximo}')
            except ValueError:
                print(f'Valor inválido, insira um número menor ou igual a {maximo}')

    def receber_decimal_entre(x, y):
        while True:
            try:
                valor = float(input(f'Digite um número decimal entre {x} e {y}'))
                if x <= valor <= y:
                    return valor
                else:
                    print(f'O número deve estar entre {x} e {y}')
            except ValueError:
                print(f'Valor inválido, insira um número decimal entre {x} e {y}')

main()