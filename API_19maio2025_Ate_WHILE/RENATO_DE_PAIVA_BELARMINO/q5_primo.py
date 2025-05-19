
import math

def main():
    n = int(input('Insira N (valor do número) > '))
    m = int(input('Insira M (limite) > '))
    i = 1
    divisores = 0
    while i <= n and n <= m:
        if n % i == 0:
            divisores += 1
            if i == n:
                if divisores <= 2:
                    print(n)
                    divisores = 0
                    n += 1
                    i = 1
                    continue
                else:
                    divisores = 0
                    n += 1
                    i = 1
            i += 1
        elif n % i != 0 :
            i += 1
            
        
       


main()