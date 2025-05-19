def receber_inteiro():
    n = float(input('Digite um numero inteiro: '))
    return n 

def receber_inteiro_positivo():
    n = float(input('Digite um numero inteiro positivo: '))

    if(n < 0):
        receber_inteiro_positivo()
    else:
        return n
    
def receber_inteiro_min_x(x):
    n =float(input('Digite um numero inteiro: '))

    if n <= float(x):
        receber_inteiro_min_x(x)
    else:
        return n

def receber_inteiro_max_x(x):
    n = float(input('Digite um inteiro: '))

    if n >= float(x):
        receber_inteiro_max_x(x)
    else:
        return n 
    
def receber_inteiro_entre_x_y(x,y):
    n = float(input('Digite um numero inteiro: '))

    if n <= float(x) or n >= float(y):
        receber_inteiro_entre_x_y(x,y)
    else:
        return n

