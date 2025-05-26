def mdc(a, b):
    # Inválida.. usou recursos não permitidos.
    while b:
        a, b = b, a % b
        return a