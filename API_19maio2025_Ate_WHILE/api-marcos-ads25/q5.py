def verificar_num_primo(numero):
     i = 1
     qtd_divisores = 0

     while i <= numero:
        if(numero % i == 0):
            qtd_divisores+=1
        i +=1
    
     if qtd_divisores == 2:
         return True
            



def main():
    n = int(input('Digite um numero: '))
    m = int(input('Digite outro numero maior: '))

    while n <= m:
        if verificar_num_primo(n):
            print(n)
        n+=1

main()