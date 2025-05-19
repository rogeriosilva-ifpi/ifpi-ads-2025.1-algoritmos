def ler_nome():
    qtd_nome = main()
    if qtd_nome % 2 == 1:
        print ("Divisores de", qtd_nome)
        i = qtd_nome
        while i >= 1:
         if qtd_nome % i == 0:
             print (i)
            
    else:
        print ("Divisores de", qtd_nome, "á",qtd_nome*qtd_nome)
        i = 1
        while i <= qtd_nome:
             print (qtd_nome * i)
             i += 1
             

def main():
    nome = input ("Digite seu nome: ")
    T = len(nome)
    print ("Tamanho do nome: ",T)
    return T

ler_nome()