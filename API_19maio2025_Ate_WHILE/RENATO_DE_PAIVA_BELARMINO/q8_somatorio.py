

def main():
    n = int(input('insira o valor de N > '))
    m = int(input('Insira o valor de M > '))
    i = 1
    soma = 0
    while i <= n and n <= m:
      if n % i == 0:
        if soma < n :
            soma += i
            i += 1
        elif soma == n:
            print(f'{n} é perfeito.')
            soma = 0
        elif soma > n:
            n += 1
            i = 1
            soma = 0
      else:
         i += 1



main()