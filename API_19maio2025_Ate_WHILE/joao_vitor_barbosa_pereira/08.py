def main():
    a = pedirNumInt("a")
    soma = 0
    contador = 1

    while contador < a:
        if a % contador == 0:
            soma += contador
        contador += 1

    if soma == a:
        print(f"{a} é um número perfeito")
    else:
        print(f"Nao é um número perfeito")


def pedirNumInt(referencia):
    try:
        value = int(input(f"Escreva o valor {referencia}: "))
        return value
    except ValueError:
        print("tente novamente")


main()