def ehPrimo(num):
    divisores = 0
    contador = 1
    
    while contador <= num:
        if num % contador == 0:
            divisores += 1
        contador += 1
        
    return divisores == 2


def obterTamanhoTexto(texto: str):
    return len(texto)


def obterTexto(label: str):
    return str(input(label))


def obterTextoTamMin(tamanhoMin: int, label: str):
    while True:
        texto = obterTexto(label)
        tamanhoTexto = obterTamanhoTexto(texto)
        if tamanhoTexto >= tamanhoMin:
            break
        else:
            print(f'Texto inválido!\nO texto deve conter no mínimo {tamanhoMin} caracteres')
    return texto


def obterNumInteiro(label: str):
    num = str(input(label))
    
    try:
        num = int(num)
        return num
    except ValueError:
        print(f'O valor "{num}" não é um número inteiro!')
        return obterNumInteiro(label)


def obterTamanhoNome(nome: str):
    return len(nome)


def controlarValores(qtdLetras):
    somatorio = 0
    qtdValores = 0
    contador = 0
    
    while True:
        contador += 1
        num = obterNumInteiro(f'{contador}° número: ')
        if ehPrimo(num):
            break
        qtdValores += 1
        somatorio += num
        
        if qtdValores == qtdLetras:
            break
        
    if qtdValores == 0:
        return 'Nenhum valor encontrado!'
    else:
        media = somatorio / qtdValores
        return f'Somatório: {somatorio}\nMédia: {media:.2f}'  
    
  
def main():
    nomeDoAnimal = obterTextoTamMin(7, 'Insira o nome do animal: ')
    qtdLetras = obterTamanhoNome(nomeDoAnimal)
    print(f'-=-ANALISANDO VALORES-=-')
    print(controlarValores(qtdLetras))    
    
    
main()    
    
        
        
        