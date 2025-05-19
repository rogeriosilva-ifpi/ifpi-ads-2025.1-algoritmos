def obterNumInteiro(label: str):
    num = str(input(label))
    
    try:
        num = int(num)
        return num
    except ValueError:
        print(f'O valor "{num}" não é um número inteiro!')
        return obterNumInteiro(label)


def somarDivisores(num):
    somatorio = 0
    contador = 1
    
    while contador < num:
        if num % contador == 0:
            somatorio += contador
        contador += 1 
        
    return somatorio

def ehNumPerfeito(num):
    somaDosDivisores = somarDivisores(num)
    return somaDosDivisores ==  num


def controlarNum(numInicial, numFinal):
    num = numInicial
    while num <= numFinal:
        if ehNumPerfeito(num):
            print(f'{num} - PERFEITO')
        else:
            print(f'{num} - NÃO PERFEITO')    
        num += 1
        
def main():
    numInicial = obterNumInteiro('Número inicial: ')
    numFinal = obterNumInteiro('Número final: ')     
    controlarNum(numInicial, numFinal)
 
main()    
    
        
        
        
        
        