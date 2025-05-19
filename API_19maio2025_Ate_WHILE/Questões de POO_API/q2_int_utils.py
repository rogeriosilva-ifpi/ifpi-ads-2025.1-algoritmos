#Questão 2
def rec_int(mensagem):
    mensagem = "Digite um número inteiro: "
    while True:
        try:
            return int(input(mensagem))
        except ValueError:
            print("Insira um número inteiro")
def rec_pos(mensagem):
    mensagem = "Digite um número inteiro positivo"
    while True:
        num = rec_int(mensagem)
        if num > 0:
            return num
        print("O número precisa ser positivo")
def rec_min(x, mensagem):
    mensagem = None
    if mensagem is None:
        mensagem = f"Digite um número inteiro"
    while True:
        num = rec_int(mensagem)
        if num >= x:
            return num
        print(f"o número deve ser pelo menos{x}.")
def rec_max(x, mensagem):
    mensagem = None
    while True:
        mensagem = rec_int(mensagem)
        if mensagem is None:
            return mensagem 
        

    
        


