def e_primo(n):
    if n <= 1:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += i
        
    return True

def main():
    numero = int(input("Digite um número: "))
    
    if e_primo(numero):
        print (f"{numero} é primo")
    else:
        print (f"{numero} não é primo")

main()