def main():

    def e_perfeito(num):
        soma_divisores = 0
        divisor = 1
        while divisor < num:
            if num % divisor == 0:
                soma_divisores += divisor
            divisor += 1
        return soma_divisores == num
    
    def verif_perfeito(N, M):
        atual = N
        while atual <= M:
            if e_perfeito(atual):
                print(f'{atual} é perfeito')
            else:
                print(f'{atual} não é perfeito')
            atual += 1

main()