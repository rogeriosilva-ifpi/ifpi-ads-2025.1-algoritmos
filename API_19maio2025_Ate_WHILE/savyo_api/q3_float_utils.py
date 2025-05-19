import random

def receber_numero_decimal(decimal: float) -> float:
    try:
        float(decimal)
        return decimal
    except ValueError:
        print("Esse número não é decimal!")
        receber_numero_decimal(input("Digite outro número: "))

def receber_numero_decimal_positivo(decimal: float) -> float:
    try:
        decimal = float(decimal)
        if decimal < 0:
            print("Esse número não é positivo!")
            receber_numero_decimal_positivo(input("Digite outro número:"))
        else:
            return decimal
    except ValueError:
        print("Esse número não é decimal!")
        receber_numero_decimal_positivo(input("Digite outro número: "))

def decimal_minimo_x(decimal: float) -> float:
    try:
        x = 10
        decimal = float(x)
        if x < 10:
            print(f"Esse número é menor que {x}!")
            decimal_minimo_x(input("Digite outro número:"))
        else:
            return decimal
    except ValueError:
        print("Esse número não é decimal!")
        decimal_minimo_x(input("Digite outro número: "))

def decimal_maximo_10(decimal: float) -> float:
    try:
        x = 10
        decimal = float(decimal)
        if decimal > x:
            print(f"Esse número é maior que {x}!")
            decimal_maximo_10(input("Digite outro número:"))
        else:
            return decimal
    except ValueError:
        print("Esse número não é decimal!")
        decimal_maximo_10(input("Digite outro número: "))


def decimal_faixa_10_100(decimal: float) -> float:
    try:
        x = 10
        y = 100
        decimal = float(decimal)
        if decimal < x and decimal > y:
            print(f"Esse número não está na faixa de {x} a {y}!")
            decimal_faixa_10_100(input("Digite outro número:"))
        else:
            return decimal
    except ValueError:
        print("Esse número não é decimal!")
        decimal_faixa_10_100(input("Digite outro número: "))

