def obterNumInteiro(label: str):
    num = str(input(label))
    
    try:
        num = int(num)
        return num
    except ValueError:
        print(f'O valor "{num}" não é um número inteiro!')
        return obterNumInteiro(label)
    
    
def obterNumInteiroPositivo(label: str):
    num = obterNumInteiro(label)
    
    while num <= 0:
        print('Entrada inválida!\nO valor deve ser positivo')
        num = obterNumInteiro(label)
    return num 

print(obterNumInteiroPositivo('.. '))    
    
    
    
    
def obterNumInteiroLimiteMin(limiteMin: int, label: str):
    num = obterNumInteiro(label)
    
    while num < limiteMin:
        print(f'Entrada inválida!\nO número deve ser maior ou igual a {limiteMin}') 
        num = obterNumInteiro(label)
    return num


def obterNumInteiroLimiteMax(limiteMax: int, label: str):
    num = obterNumInteiro(label)
    
    while num > limiteMax:
        print(f'Entrada inválida!\nO número deve ser menor ou igual a {limiteMax}') 
        num = obterNumInteiro(label)
    return num


def obterNumInteiroNaFaixa(limiteMin: int, limiteMax: int, label: str):
    num = obterNumInteiro(label)
    
    while num < limiteMin or num > limiteMax:
        print(f'Entrada inválida!\nO número deve está entre {limiteMin} e {limiteMax}') 
        num = obterNumInteiro(label)
    return num


        
        
        