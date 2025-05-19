def validar(mensagem, tipo):
    while True:
        try:
            valor = input(mensagem)
            if valor.isdigit():
                return tipo(valor)
            else:
                print('Valor inválido')
        except ValueError():
            print('Digite um valor numérico')
            continue
       
    
#1
'''def tamanho_nome():
    nome = validar('Insira seu nome:  ', str)
    tamanho_nome = int(len(nome)) 
    if tamanho_nome % 2 != 0:'''
         
#2   
'''def num_inteiro_positivo():
    num_int_positivo = validar('DIgite um numero INTEIRO positivo ', int)
    if num_int_positivo > 0:
        print(f'{num_int_positivo} É um número inteiro')
    else:
         print('Numero inválido, digite um numero inteiro')        
num_inteiro_positivo()


#3   
def num_decimal():
        decimal = validar('Digite um numero decimal ', str)
        if str(decimal):
        return decimal.replace(',','.').strip()
        
num_decimal()'''

#4A
'''def obter_texto():
    texto = input('Digite um texto:  ')
    print(texto)
obter_texto()

#4B
def texto_minimo_maximo():
    texto = input('Digite um texto com no mínimo 8 caracteres e no máximo 30 caracteres:  ')
    tamanho_texto = len(texto)
    if tamanho_texto < 8 or tamanho_texto > 30:
        print('Texto fora da faixa de caracteres')
    else:
        print(f'Aqui está seu texto:\n {texto}')
texto_minimo_maximo()

#5
def numero_primo():
'''

#9
def emprestimo_joao():
    renda_mensal = validar('Qual a sua renda mensal?  ', float) 
    valor_emprestimo = validar('Qual o valor do emprestimo?  ', float)    
    prazo_desejado = validar('Qual o prazo que vc deseja pagar(em meses)?  ', int)
    
    if prazo_desejado < 2 or prazo_desejado > 24:
        print('Prazo fora da faixa disponível (2 a 24 parcelas)!')
    elif valor_emprestimo < 1518:
        print('O valor mínimo de um emprestimno é de 1.518,00 reais')
    emprestimo_maximo = renda_mensal * 0.30 
    if valor_emprestimo > emprestimo_maximo:
        print('Nao e possivel fazer o emprestimo, pois o valor ultrapassa 30 porcento da sua renda')
    
   selic = valor_emprestimo * 0.1475 
   iof = (valor_emprestimo * 0.0038) + ((prazo_desejado * 30) * 0.000082 )
   montante =  valor_emprestimo + juros_final
   taxa_seis_parcelas = selic * 0.50
   taxa_doze_parcelas = selic * 0.75
   taxa_dezoito_parcelas = selic
   taxa_mais_dezoito = selic * 1.30
   
  
   
   
   print(iof)
    
emprestimo_joao()