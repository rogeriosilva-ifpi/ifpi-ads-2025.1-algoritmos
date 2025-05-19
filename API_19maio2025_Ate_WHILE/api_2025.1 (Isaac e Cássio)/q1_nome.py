from q4_text_utils import obter_texto


def main():
    nome = obter_texto('Digite seu nome: ')
    tamanho = len(nome)

    contador_par = 1
    contador_impar = 1

    if eh_par(tamanho):
        print(f'Todos os multiplos de 1 até tamanho do nome({tamanho}):')

        while contador_par <= tamanho:
            multiplo = tamanho * contador_par
            print(f'{tamanho} x {contador_par} = {multiplo}')
            contador_par += 1

    else:
        print(f'Todos os divisores de tamanho do nome({tamanho}) até 1:')
        while contador_impar <= tamanho:
            if tamanho % contador_impar == 0:
                print(contador_impar)
            contador_impar += 1


def eh_par(num: int):
    return num % 2 == 0


main()