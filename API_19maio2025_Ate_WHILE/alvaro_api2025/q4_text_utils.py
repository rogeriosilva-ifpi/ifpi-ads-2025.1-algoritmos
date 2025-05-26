def obter_texto(label):
    texto = input(label)
    return texto

def obter_txt_min(label):
    # faltou receber o parâmetro de limite mínimo
    tam_min = int(input('Infome o tamanho mínimo do texto: '))
    texto = input(label)
    tamn_texto = len(texto)
    if tamn_texto < tam_min:
        print('Textp inválido, por favor tente novamente')
        return obter_txt_min(label)
    else:
        return texto
    
def obter_txt_max(label):
    # idem.
    tam_min = int(input('Infome o tamanho máximo do texto: '))
    texto = input(label)
    tamn_texto = len(texto)
    if tamn_texto > tam_min:
        print('Textp inválido, por favor tente novamente')
        return obter_txt_min(label)
    else:
        return texto
    
def obter_txt_xy(label:str):
    # nome ruim.. faltou parametros
    numX = int(input('Informe um número para ser o limite mínimo: '))
    numY = int(input('Informe um número para ser o limte mínimo: '))
    texto = input(label)
    tam_txt = len(texto)
    if tam_txt < numX or tam_txt > numY:
        print('Texto inválido, tente novamente')
        return obter_txt_xy(label)
    else:
        return texto