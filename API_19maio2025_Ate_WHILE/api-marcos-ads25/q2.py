def receber_inteiro():
    n = int(input('Digite um numero inteiro: '))
    return n 

def receber_inteiro_positivo():
    n = int(input('Digite um numero inteiro positivo: '))
    
    if(n < 0):
        receber_inteiro_positivo()
    else:
        return n
    
def receber_inteiro_min_x(x):
    n = int(input('Digite um numero inteiro: '))

    if n <= int(x):
        receber_inteiro_min_x(x)
    else:
        return n

def receber_inteiro_max_x(x):
    n = int(input('Digite um inteiro: '))

    if n >= int(x):
        receber_inteiro_max_x(x)
    else:
        return n 
    
def receber_inteiro_entre_x_y(x,y):
    n = int(input('Digite um numero inteiro: '))

    if n <= int(x) or n >= int(y):
        receber_inteiro_entre_x_y(x,y)
    else:
        return n



