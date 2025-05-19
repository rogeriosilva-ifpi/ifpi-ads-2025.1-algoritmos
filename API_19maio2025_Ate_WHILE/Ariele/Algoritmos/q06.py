def main():
    texto = obter_texto('Digite o nome do animal: ')
    
    qtd = 0
    soma = 0
    
    
    while qtd < len(texto):
        numero = int(input('Digite um número: '))
        soma += numero
        qtd += 1
        media = soma / qtd
        
    print(f"Número{qtd} - Somatório: {soma} - Média: {media:.2f}")
    print('')
    
def obter_texto(label:str):
   texto = input (label)
   try :
        text = str(texto)
        if len(text) < 7:
            print(f'O tamanho minimo é de 7 caracteres')
            return obter_texto(label)
        return text
   except ValueError:
       print('Digite um texto válido')
       return obter_texto(label)
        
    
main()