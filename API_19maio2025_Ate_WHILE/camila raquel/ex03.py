def obterNumReal(label: str):
    num = str(input(label))
    
    try:
        num = float(num)
        return num
    except ValueError:
        print(f'O valor "{num}" não é um número real!')
        return obterNumReal(label)
    
    
def obterNumRealLimiteMin(limiteMin: float, label: str):
    num = obterNumReal(label)
    
    while num < limiteMin:
        print(f'Entrada inválida!\nO número deve ser maior ou igual a {limiteMin}') 
        num = obterNumReal(label)
    return num


def obterNumRealLimiteMax(limiteMax: float, label: str):
    num = obterNumReal(label)
    
    while num > limiteMax:
        print(f'Entrada inválida!\nO número deve ser menor ou igual a {limiteMax}') 
        num = obterNumReal(label)
    return num


def obterNumRealNaFaixa(limiteMin: float, limiteMax: float, label: str):
    num = obterNumReal(label)
    
    while num < limiteMin or num > limiteMax:
        print(f'Entrada inválida!\nO número deve está entre {limiteMin} e {limiteMax}') 
        num = obterNumReal(label)
    return num

print(obterNumRealNaFaixa(1, 10, 'nota: '))


        