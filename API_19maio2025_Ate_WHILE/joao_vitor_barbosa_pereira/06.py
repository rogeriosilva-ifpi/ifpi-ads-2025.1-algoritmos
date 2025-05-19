def main():
    a = pedirNumInt("a")
    b = pedirNumInt("b")
    mdc = a if a < b else b

    while True:
        if mdc % a == 0 and mdc % b == 0:
            print(f"o mdc de {a} e {b} é {mdc}")
            break
        mdc += 1


def pedirNumInt(referencia):
    try:
        value = int(input(f"Escreva o valor {referencia}: "))
        return value
    except ValueError:
        print("tente novamente")
        return pedirNumInt(referencia)


main()