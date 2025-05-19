def main():

    numero = int(input('Digite um valor: '))
    numero2 = int(input('Digite um outro valor: '))

    if numero % 3 == 1 and numero2 % 3 == 1:
        print('E primo')

    print(f' os valores n:{numero} a {numero2} sao primos')

main()


