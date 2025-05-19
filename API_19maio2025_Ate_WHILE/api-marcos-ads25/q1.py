def verifica_numero(tamanho):
    p = 1
    i = tamanho 
    if tamanho % 2 == 0:
        while p < tamanho:
            print(f'{tamanho*p}')
            p+=1 
    else:
        while i >= 1:
            if tamanho % i == 0:
                print(f'{i} é divisor de {tamanho}')
            i = i -1




def main():
    nome = input("Digite seu nome: ")
    tamanho = len(nome)

    print(f'A palavra {nome} tem {tamanho} caracteres')

    verifica_numero(tamanho)


main()