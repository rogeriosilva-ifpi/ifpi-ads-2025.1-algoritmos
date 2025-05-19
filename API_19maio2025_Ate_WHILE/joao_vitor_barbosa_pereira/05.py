def main():
    a = pedirNumInt("a")
    soma = 0
    contador = 1

    while contador < (a + 1):
        if a % contador == 0:
            soma += contador
        contador += 1

    if soma == a + 1:
        print(f"{a} é um número primo")
    else:
        print(f"Nao é um número primo")


def pedirNumInt(referencia):
    try:
        value = int(input(f"Escreva o valor {referencia}: "))
        return value
    except ValueError:
        print("tente novamente")


main()