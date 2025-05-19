def main():
    texto = obter_texto('Digite um texto: ',10, 15)
    ...
    
def obter_texto(label:str, min_tamanho: int, max_tamanho: int):
   texto = input (label)
   try :
        text = str(texto)
        if len(text) < min_tamanho:
            print(f'O tamanho minimo de caracteres é de: {min_tamanho}')
            return obter_texto(label,min_tamanho, max_tamanho)
        if len(text) > max_tamanho:
            print(f'O tamanho máximo de caracteres é de: {max_tamanho}')
            return obter_texto(label,min_tamanho,max_tamanho)
        return text
   except ValueError:
       print('Digite um texto válido')
       return obter_texto(label,min_tamanho, max_tamanho)
        
    
main()