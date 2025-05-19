from q2_int_utils import receber_int_positivo
import math

def num_eh_primo():
    numero_min = receber_int_positivo('Digite um número mínimo: ')
    numero_max = receber_int_positivo('Digite um número máximo: ')

    numero = numero_min

    while numero <= numero_max:

        if numero == 1:
            print(f'{numero} não é primo')
        elif numero == 2:
            print(f'{numero} é primo')
        else:
            contador = 1
            while contador <= int(math.sqrt(numero)):
                if numero % contador == 0 and contador  != 1 and contador != numero:
                    primo = False
                    break
                
                contador += 1
            if primo:
                print(f'Número {numero} é primo')
            else:
                print(f'Número {numero} não é primo')

        numero += 1
            

num_eh_primo()