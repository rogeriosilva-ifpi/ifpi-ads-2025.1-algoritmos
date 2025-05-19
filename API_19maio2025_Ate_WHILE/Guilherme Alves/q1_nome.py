from q4_text_utils import obter_texto
def main():
    nome = obter_texto("Digite o seu nome: ")
    tamanho_nome = len(nome)
    if tamanho_nome % 2 != 0:
        contador = 1
        while contador <= tamanho_nome:
            if tamanho_nome % contador == 0:
                print(contador)
            contador += 1
    else:
        contador = 2
        while contador <= (tamanho_nome + 1):
            multiplos = tamanho_nome * contador
            print(multiplos)
            contador += 1

main()