def main():
    nome = obter_texto('Qual se nome? ')

    nome2 = obter_texto_minimo('', 10)

    nome3 = obter_texto_maximo('', 70)

    nome4 = obter_texto_faixa('', 10, 70)



def obter_texto(label):
    return input(label)


def obter_texto_minimo(label, tamanho_min):
    tamanho_min = input("tamanho minimo: ")
    nome = obter_texto('Qual o nome')
    if len(nome) > tamanho_min:
        return obter_texto_minimo()


def obter_texto_maximo(label, tamanho_max):
    tamanho_max = input("tamanho maximo: ")
    nome = obter_texto('Qual o nome') 
    if len(nome) < tamanho_max:
        return obter_texto_maximo(label, tamanho_max)


def obter_texto_faixa(label, tamanho_max, tamanho_min):
    tamanho_min = input("tamanho minimo: ")
    tamanho_max = input("tamanho maximo: ")
    nome = obter_texto('Qual o nome') 
    if tamanho_min < len(nome) < tamanho_max:
        return obter_texto_faixa(label, tamanho_max, tamanho_min)
    

main()

