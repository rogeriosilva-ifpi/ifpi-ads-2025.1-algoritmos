def main():
    
    valor = int(input('Digite um numero:'))
    valor_n = int(input('Digite um numero:'))
           
    if valor == float:
        print('Nao e permitidos numeros com casas decimais!!!')
    else:
        return valor
    
    if valor_n < 1:
        print('Numeros Negativos nao sao permitidos e sim so numeros positivos!!')
    else:
         return valor_n
    
    print(f'Numero Inteiro:{valor} \n Numero Positivo:{valor_n}')

main()
