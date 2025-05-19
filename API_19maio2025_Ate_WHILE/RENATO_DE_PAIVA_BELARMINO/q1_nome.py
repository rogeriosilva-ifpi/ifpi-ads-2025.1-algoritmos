

def main():
    nome = input('insira seu nome > ')
    if len(nome) % 2 != 0:
        i = 1
        while i <= len(nome):
            if len(nome) % i == 0:
              print(i)
              i += 1
              continue
            else:
                i += 1
                continue
    elif len(nome) % 2 == 0:
        t = len(nome)
        i = 1
        while i < t:
            print(t * (i + 1))
            i += 1





main()