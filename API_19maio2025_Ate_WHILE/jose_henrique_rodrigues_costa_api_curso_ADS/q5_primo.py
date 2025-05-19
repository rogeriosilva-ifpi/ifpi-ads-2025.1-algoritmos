import math

# Questão 5)
def primo():
    intervalo_minimo = int(input('Número mínimo do intervalo: '))
    intervalo_maximo = int(input('Número máximo do intervalo: '))
    numero_inteiro = int(input('Digite o mesmo número que foi usado como mínimo do intervalo: '))

    while numero_inteiro < intervalo_maximo:
        numero_inteiro += 1
        raiz_quadrada = math.sqrt(numero_inteiro)
        if raiz_quadrada % 2 != 0 and raiz_quadrada % 3 != 0 and raiz_quadrada % 5 != 0 and raiz_quadrada % 7 != 0:
            print(f'{numero_inteiro} é um número primo')
            

executar_primo = primo()
    

