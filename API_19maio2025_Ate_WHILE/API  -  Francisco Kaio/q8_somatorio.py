# recursos inválidos
def e_perfeito(n):
    soma = sum([i for i in range(1, n) if n % i == 0])
    return soma

def nao_perfeito(n, m):
    for n in range (n, m + 1):
        if e_perfeito(n):
            print (f"{n} é perfeito")
        else:
            print (f"{n} não é perfeito")