'''def validar(mensagem, tipo):
    while True:
        try:
            valor = input(mensagem, tipo)
            if valor == int:
                return int(valor)
            elif valor == str and valor.isdigit():
                return float(valor).replace(',', '.').strip()
            elif valor == str:
                return str(valor)   
        except valueError():
            print('Valor inválido, digite novamente')
            continue
       
    

def tamanho_nome():
    nome = validar('Insira seu nome:  ', str)
    if len(nome)''' 
    
    
def num_inteiro_positivo():
    num_int_positivo = int(input('DIgite um numero INTEIRO  '))
    if num_int_positivo >= 0:
        print(f'{numero_int}É um número inteiro')
    else:
         print('Numero inválido, digite um numero inteiro')
         
num_inteiro_positivo()
        