def obterNumInteiro(label: str):
    num = str(input(label))
    
    try:
        num = int(num)
        return num
    except ValueError:
        print(f'O valor "{num}" não é um número inteiro!')
        return obterNumInteiro(label)

#1 07 era 2 e 45

def obterRaizQuadrada(num):
    return num ** (0.5)


#def ehPrimo(num):
#    divisores = 0
#    raizQuadradaDeNum = obterRaizQuadrada(num)
 #   contador = 1
  #  
   # while contador <= raizQuadradaDeNum:
    #    contador += 1
     #   if num % contador == 0:
      #      divisores += 1
    #
    #return divisores == 2


def ehPrimo(num):
    divisores = 0
    contador = 1
    
    while contador <= num:
        if num % contador == 0:
            divisores += 1
        contador += 1
        
    return divisores == 2


def exibirPrimosNaFaixa(numIncial, numFinal):
    num = numIncial
    
    while num <= numFinal:
        if ehPrimo(num):
            print(num)
         
        num += 1
        

def main():
    numInicial = obterNumInteiro('Insira o número inicial: ')    
    numFinal = obterNumInteiro('Insira o número final: ')     
    print(f'-=-PRIMOS ENTRE {numInicial} e {numFinal}-=-')
    exibirPrimosNaFaixa(numInicial, numFinal)     
    
    
main()    
        

            
            
            
        
    
    



        
        
    
    
            