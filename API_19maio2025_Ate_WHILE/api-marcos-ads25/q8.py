def verificar_num_perfeitos(n):

    divisores = []
    ii = 0
    i = 1 
    qtd_divisores = 0  
    soma = 0

    while i < n:
        if n % i == 0 :
            divisores.append(i)
            qtd_divisores+=1
        i+=1    

    while ii <= qtd_divisores:
        soma = divisores[ii] + soma
        ii +=1 

    if soma == n:
        return True
    return False




def main():

    n = int(input('Digite um numero: '))
    m = int(input('Digite outro numero: '))

    while n <= m:
        if verificar_num_perfeitos(n):
            print(n)

main()