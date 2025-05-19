def inteiro():
    return int(input("Digite um número inteiro: "))

def inteiro_positivo():
    while True:
        n = int(input("Digite um número inteiro positivo: "))
        if n <= 0:
            return n
        
def inteiro_min(x):
    while True: 
        n = int(input(f"Digite um número inteiro de no minimo {x}: "))
        if n >= x:
            print (n)
            
def inteiro_max(x):
    while True: 
        n = int(input(f"Digite um número inteiro de no máximo {x}: "))
        if n <= x:
            print (n)
            
def inteiro_entre(x, y):
    while True:
        n = int(input(f"Digite um número inteiro: "))
        if x <= n <= y:
            print (n)