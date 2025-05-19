def ehImpar(num: int):
    return num % 2 == 1


def ehPar(num: int):
    return num % 2 == 0


def obterTamanhoNome(nome: str):
    return len(nome)


def mostrarDivisores(num):
    contador = num
    
    while contador >= 1:
        if num % contador == 0:
            print(contador)
        contador -= 1
        
        
def mostrarMultiplos(num):
    contador = 1
    
    while contador <= num:
        contador += 1
        print(num * contador)      
       
def analisarNome(tamanhoNome: int):
    if ehImpar(tamanhoNome):
        print(f'-=-Divisores de {tamanhoNome}-=-')  
        mostrarDivisores(tamanhoNome)  
        
    if ehPar(tamanhoNome):
        print(f'-=-Os {tamanhoNome} próximos múltiplos de {tamanhoNome}-=-')
        mostrarMultiplos(tamanhoNome)
               
            
        
def main():
    print('-=-ANALISADOR DE NOMES-=-')
    nome = str(input('Insira seu nome: '))
    tamanhoNome = obterTamanhoNome(nome)
    
    analisarNome(tamanhoNome)
    
main()    
    
    