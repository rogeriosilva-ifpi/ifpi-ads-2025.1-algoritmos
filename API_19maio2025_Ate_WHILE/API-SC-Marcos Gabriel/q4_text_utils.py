def obter_texto():
    texto = str(input("Digite o texto: "))
    return texto


def texto_tamanho_maximo():
    texto = str(input("Digite o texto: "))
    tamanho = len(texto)
    return max(tamanho)

def texto_tamanho_mínimo():
    texto = str(input("Digite o texto: "))
    tamanho = len(texto)
    return min(tamanho)

def texto_tamanho_maximo_e_mínimo():
    texto = str(input("Digite o texto: "))
    tamanho = len(texto)
    return min(tamanho) and max(tamanho)