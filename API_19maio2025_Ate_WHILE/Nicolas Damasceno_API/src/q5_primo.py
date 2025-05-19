from math import sqrt
def numero_primo(num):
    raiz = sqrt(num)
    divisivel = 1
    while divisivel <= raiz:
        if num % divisivel == 0:
            return False
        divisivel += 1
    return True

def main():
    numero_inicial = int(input('Digite um número inicial N: '))
    numero_final = int(input('Digite o número final M: '))
    contador = numero_inicial
    while contador < numero_final:
        contador += 1
        primo = numero_primo(contador)
        if primo:
            print(f'Primo {primo}')

if __name__ == '__main__':
    main()