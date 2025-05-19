from utils import obterTamanhoTexto

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


def obterTextoTamMax(tamanhoMax: int, label: str):
    while True:
        texto = obterTexto(label)
        tamanhoTexto = obterTamanhoTexto(texto)
        if tamanhoTexto <= tamanhoMax:
            break
        else:
            print(f'Texto inválido!\nO texto deve conter no máximo {tamanhoMax} caracteres')
    return texto


def obterTextoTamMinMax(tamanhoMin: int, tamanhoMax: int, label: str):
    while True:
        texto = obterTexto(label)
        tamanhoTexto = obterTamanhoTexto(texto)
        if tamanhoTexto >= tamanhoMin and tamanhoTexto <= tamanhoMax:
            break
        else:
            print(f'Texto inválido!\nO texto deve conter no mínimo {tamanhoMin} caracteres e no máximo {tamanhoMax} caracteres')
    return texto

print(obterTextoTamMinMax(3, 7, 'Nome; '))


     
     
     
    
    

    