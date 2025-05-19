from q3_float_utils import obter_real
def main():

    n = obter_real("N(limite inferior): ")
    m = obter_real("M(limite superior): ")
    while n <= m:
        if e_perfeito(n):
            print(f"{n} é perfeito")
        else:
            print(f"{n} não é perfeito")
        n += 1
    
def e_perfeito(num):
    soma_divisores = 0
    contador = 1
    while contador < num:
        if num % contador == 0:
            soma_divisores += contador
        contador += 1
    if soma_divisores == num:
        print("perfeito")
        return True
    else:
        return False


main()
