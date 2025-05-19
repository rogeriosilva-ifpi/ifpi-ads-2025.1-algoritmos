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


def obterMenor(n1: int, n2: int):
    return n1 if n1 < n2 else n2


def obterMDC(n1: int, n2: int):
    menor = obterMenor(n1, n2)
    canditadoDivisor = 1
    
    while canditadoDivisor <= menor:
        if n1 % canditadoDivisor == 0 and n2 % canditadoDivisor == 0:
            mdc = canditadoDivisor
        canditadoDivisor += 1
        
    return mdc


def main():
    n1 = obterNumInteiroPositivo('Insira o 1° número: ')
    n2 = obterNumInteiroPositivo('Insira o 2° número: ')
    mdc = obterMDC(n1, n2)
    print(f'O MDC de ({n1}, {n2}) é {mdc}')
    
main()    
    