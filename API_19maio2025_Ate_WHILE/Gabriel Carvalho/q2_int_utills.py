def main():
    # Funcao dentro de funcao

    def receber_inteiro():
        while True:
            try:
                valor = int(input('Digite um número inteiro: '))
                return valor
            except ValueError:
                print('Valor inválido. Digite um número inteiro')

    def receber_inteiro_positivo():
        while True:
            try:
                valor = int(input('Digite um número inteiro positivo: '))
                if valor > 0:
                    return valor 
                else:
                    print('O valor deve ser positivo')
            except ValueError:
                print('Valor inválido, por favor digite um número inteiro positivo')

    def receber_inteiro_minimo(minimo):
        while True:
            try:
                valor = int(input(f'Digite um número inteiro maior ou igual a {minimo}'))
                if valor >= minimo:
                    return valor
                else:
                    print(f'O número deve ser maior ou igual a {minimo}')
            except ValueError:
                print(f'Valor inválido, insira um número maior ou igual a {minimo}')

    def receber_inteiro_maximo(maximo):
        while True:
            try:
                valor = int(input(f'Digite um número inteiro menor ou igual a {maximo}'))
                if valor <= maximo:
                    return valor
                else:
                    print(f'O número deve ser menor ou igual a {maximo}')
            except ValueError:
                print(f'Valor inválido, insira um número menor ou igual a {maximo}')

    def receber_inteiro_entre(x, y):
        while True:
            try:
                valor = int(input(f'Digite um número inteiro entre {x} e {y}'))
                if x <= valor <= y:
                    return valor
                else:
                    print(f'O número deve estar entre {x} e {y}')
            except ValueError:
                print(f'Valor inválido, insira um número entre {x} e {y}')

main()