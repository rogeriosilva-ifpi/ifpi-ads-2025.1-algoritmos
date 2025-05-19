from q3_float_utils import obter_real
import math
def main():

    n = obter_real("N(limite inferior): ")
    m = obter_real("M(limite superior): ")

    while n <= m:
        if obter_primo(n):
            if n != 1:
                print(n)
        n += 1

def obter_primo(num):
    num_int = int(num)
    limite = math.sqrt(num_int)
    contador = 1
    quant_divi = 0
    while contador <= 500 and contador <= limite:
        if num % contador == 0:
            quant_divi += 1
        contador += 1
    if quant_divi < 2:
        return True
    else:
        return False
              
main()