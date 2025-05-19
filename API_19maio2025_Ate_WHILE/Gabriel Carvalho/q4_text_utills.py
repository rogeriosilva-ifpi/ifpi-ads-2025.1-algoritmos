def main():

    def obter_texto(mensagem='Digite um texto: '):
        return input(mensagem)
    
    def contar_caracteres(texto):
        contador = 0
        try:
            while True:
                texto[contador]
                contador += 1
        except IndexError:
            return contador
    
    def obter_texto_com_tamanho(mensagem='Digite um texto: ', minimo=None, maximo=None):
        while True:
            texto = input(mensagem)
            tamanho = contar_caracteres

            if minimo is None and tamanho < minimo:
                print(f'O texto deve ter no minimo {minimo} caracteres')
                continue

            if maximo is None and tamanho > maximo:
                print(f'Você ultrapassou os caracteres maximos de {maximo}')
                continue

            return texto
        
main()