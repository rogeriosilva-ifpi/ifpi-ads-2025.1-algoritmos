def variaveis():
 prazo_desejado = int()
valor_emprestimo = () 
selic = 0.1475
 

def main():
 salario_minimo = float(input("Digite o valor da sua Renda Mensal: "))
 valor_emprestimo = int(input("Digite o valor do Empréstimo a ser tomado: "))
 prazo_desejado = int(input("Digite o valor do prazo do empréstimo: "))

 while True:
    try:
        if prazo_desejado <= 6:
            selic * 0.50
        elif 7 >= prazo_desejado <= 12:
            selic * 0.75
        elif 12 > prazo_desejado <= 18:
            selic * 0.100
        elif 18 > prazo_desejado <= 24:
            selic * 0.130
          
    except ValueError :
        print("digite apenas as parcelas disponíveis (de 6x até 24x)")
        break
    valor_min_emprestimo = salario_minimo;
    print(f"O valor mínimo de empréstimo é: R${valor_min_emprestimo}" )

    valor_max_emprestimo = salario_minimo * 0.03
    print(f"O valor máximo de parcela é: R${valor_max_emprestimo}" )

    calculo_imposto  = (0.038 * valor_emprestimo) + (0.000082 * prazo_desejado)
    print(f"O valor do IOF é igual a: {calculo_imposto:.2f}")



if __name__ == "__main__":
    main()



 
    







main()