

def main():

    import math
    
    def e_primo(n):
        if n < 2:
            return False
        divisor = 2
        limite = int(math.sqrt(n))
        while divisor <= limite:
            if n % divisor == 0:
                return False
            divisor += 1
        return True
    
    def imprimir_primo(n, m):
        atual = n
        while atual <= m:
            if e_primo(atual):
                print(atual)
            atual += 1
            
main()