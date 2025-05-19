def main():

    def tamanho_string(texto):
        contador = 0
        try:
            while True:
                texto[contador]
                contador += 1
        except IndexError:
            return contador
    
    nome = input(f'Digite o seu nome: ')
    tamanho = tamanho_string(nome)    
    
    

    if tamanho % 2 == 1:
        print(f'Divisores de tamanho {tamanho}')
        divisor = tamanho
        while divisor >= 1:
             if tamanho % divisor == 0:
                print(divisor)
                divisor -= 1

    else:
        print(f'Próximos {tamanho} múltiplos de {tamanho}')
        contador = 1
        while contador <= tamanho:
            print(tamanho * contador)
            contador += 1
            
main()