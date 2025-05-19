def main():
    nome = str(input('Digite seu nome: '))

    for i in range(len(nome)):
        if i % 2 == 0:
            return i * nome 
        elif i % 2 == 2:
            return i * nome
    
main()


    
       
