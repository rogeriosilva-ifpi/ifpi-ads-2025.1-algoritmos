import random

def receber_numero_inteiro() -> int:
    return random.randint(-100000, 100000)

def receber_numero_inteiro_positivo(inteiro: int) -> int:
    return random.randint(0, 100000)

def inteiro_minimo_x(x: int) -> int:
    try:
        x = int(x)
        return random.randint(x, 1000000)
    except ValueError:
        print("Esse número não é inteiro!")
        inteiro_minimo_x(input("Digite outro número: "))

def inteiro_maximo_x(x: int) -> int:
    try:
        x = int(x)
        return random.randint(-100000, x)
    except ValueError:
        print("Esse número não é inteiro!")
        inteiro_maximo_x(input("Digite outro número: "))


def inteiro_faixa_x_y(x: int, y: int) -> int:
    try:
        x = int(x)
        y = int(y)
        return random.randint(x, y)
    except ValueError:
        print("Esse número não é inteiro!")
        inteiro_faixa_x_y(input("Digite outro x: "), input("Digite outro y: "))
