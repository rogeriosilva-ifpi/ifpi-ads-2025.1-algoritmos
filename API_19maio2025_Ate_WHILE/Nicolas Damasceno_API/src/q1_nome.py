# Função Principal
def main():
    # Entrada de Dados
    nome = input('Digite um nome: ')
    tamanho = len(nome)
    # Processamento
    if tamanho % 2 == 0:
        contador = 0
        multiplo = tamanho
        print(f'Os múltiplos com o mesmo tamanho {tamanho} do nome {nome}')
        while contador < tamanho:
            multiplo += tamanho
            # Saída
            print(f'Múltiplo {multiplo}')
            contador += 1
    elif tamanho % 2 != 0:
        divisor = 1
        print(f'Os divisores do tamanho {tamanho} do nome {nome}')
        while divisor <= tamanho:
            if (tamanho % divisor) == 0:
                # Saída
                print(f'Divisor {divisor}')
            divisor += 1

if __name__ == '__main__':
    main()