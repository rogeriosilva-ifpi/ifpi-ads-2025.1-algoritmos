def main():

    def mdc(a, b):
        while b != 0:
            resto = a % b
            a = b
            b = resto
        return a 

    while True:
        try:
            num1 = int(input('Digite o primeiro número: '))
            num2 = int(input('Digite o segundo número: '))
            if num1 > 0 and num2 > 0:
                break
            else:
                print('Os números devem ser inteiros e positivos')
        except ValueError:
            print('Inválido. Digite números inteiros positivos')

    resultado = mdc(num1, num2)
    print(f'O MDC de {num1} e de {num2} é igual a {resultado}')

main()