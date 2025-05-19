from q4_text_utils import obter_texto_min
from q2_int_utils import obter_int
import math
def main():

    nome = obter_texto_min("Digite o nome do animal: ",7)
    contador = 1
    soma = 0
    quant_num = 0
    while contador <= len(nome):
        num = obter_int(f"Digite o {contador}° número: ")
        if obter_primo(num):
            break
        else:     
            soma += num
            contador += 1
            quant_num += 1
        
    media = soma / quant_num

    resultado = f'''
    Soma dos valores digitados: {soma}
    Média dos valores digitados: {media:.2f}
    '''

    print(resultado)

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