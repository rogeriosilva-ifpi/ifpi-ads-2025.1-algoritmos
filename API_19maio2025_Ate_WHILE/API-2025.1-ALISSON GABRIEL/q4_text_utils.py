def text_utils():
    def obter_texto():
        texto = input('Escreva seu texto: ')

    obter_texto()

    def obter_texto_min_e_max():
        minimo = int(input('Digite a quantidade mínima de caracteres: '))
        maximo = int(input('Digite a quantidade máxima de caracteres: '))
        obter_texto()
        while len(obter_texto) > maximo and len(obter_texto) < minimo:
            print('O tamanho do texto não está na faixa informada. Refaça seu texto por favor.')    
        obter_texto()

    obter_texto_min_e_max()    

text_utils()    