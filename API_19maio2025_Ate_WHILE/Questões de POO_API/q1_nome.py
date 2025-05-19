#Questão 1
def num_divisor(n):
    return [i for i in range(n, 0, -1) if n % i == 0]

def num_multi(n):
    return [n * i for i in range (1, n + 1)]

nome = input("Digite seu noe: ")
tamanho = len(nome)

if nome % 2 == 1:
    print(f"Tamanho do nome ({tamanho}) é ímpar. Divisores até 1: ")

else:
    print(f"O Tamanho do nome ({tamanho})é par. Múltiplos de ({tamanho}):")
    print(num_multi(tamanho))


