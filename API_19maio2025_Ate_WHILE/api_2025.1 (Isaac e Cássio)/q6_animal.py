from q4_text_utils import obter_texto_min
from math import sqrt
from q2_int_utils import obter_numero_inteiro


def main():
    nome_animal = obter_texto_min('Nome do animal: ', 7)
    tamanho_nome = len(nome_animal)

    soma = 0

    while True:
        qtd_num = obter_numero_inteiro('Digite um número: ')

        if qtd_num == tamanho_nome:
            break

        if not eh_primo(qtd_num):
            soma += qtd_num

    media = soma / tamanho_nome

    print(f'Somatório: {soma}\nMédia: {media:.2f}')


def eh_primo(n: int):
    raiz = sqrt(n)
    contador = 2
    divisores = 0

    while contador <= raiz:
        if raiz % contador == 0:
            divisores += 1
        contador += 1

    if n == 1:
        return False
    if 0 < divisores < 2:
        return True
    else:
        return False
    

main()