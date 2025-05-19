def obter_numero_intero(label):
    valor_int = input(label)
    try:
        numero_int = int(valor_int)
        return numero_int
    except ValueError:
        print(f"O valor que você passou '{valor_int}' não é um número interio ")
        return obter_numero_intero(label)
        

def obter_numero_intero_positivo(label):
    valor_positivo = input(label)
    try:
        numero_positivo = int(valor_positivo)
        if valor_positivo > 0:
            return numero_positivo
        else:
            print("O seu número '{numero_positivo}' tem que ser positivo(maior que zero).")
            return obter_numero_intero_positivo(label)    
    except ValueError:
        print(f"O valor que você passou '{valor_positivo}' não é um número inteiro positivo(maior que zero).")
        return obter_numero_intero_positivo(label)
        
        
def obter_numero_intero_minimo(label, valor_min: int,):
    valor_min = int(input("Insira o valor mínimo: "))
    valor_maior_min = input(label)
    try:
        numero_maior_min = int(valor_maior_min)
        if numero_maior_min > valor_min:
            return numero_maior_min
        else:
            print("O seu número '{numero_maior_min}' não é maior que 7).")
            return obter_numero_intero_minimo(label)    
    except ValueError:
        print(f"O valor que você passou '{valor_maior_min}' não é um número inteiro positivo(maior que zero).")
        return obter_numero_intero_minimo(label)
        

def obter_numero_intero_maximo(label, valor_max: int):
    valor_max = int(input("Insira o valor máximo: "))
    valor_menor_max = input(label)
    try:
        numero_menor_max = int(valor_menor_max)
        if numero_menor_max < valor_max:
            return numero_menor_max
        else:
            print("O seu número '{numero_menor_max}' não é menor que 100).")
            return obter_numero_intero_maximo(label)    
    except ValueError:
        print(f"O valor que você passou '{valor_menor_max}' não é um número inteiro positivo(maior que zero).")
        return obter_numero_intero_maximo(label)
        

def obter_numero_intero_faixa(label, valor_min: int, valor_max: int):
    valor_min = int(input("Insira o valor mínimo: "))
    valor_max = int(input("Insira o valor máximo: "))
    valor_faixa = input(label)
    try:
        numero_faixa = int(valor_faixa)
        if valor_min < numero_faixa < valor_max:
            return numero_faixa
        else:
            print("O seu número '{numero_faixa}' deve estar entre 7 e 100).")
            return obter_numero_intero_faixa(label)    
    except ValueError:
        print(f"O valor que você passou '{valor_faixa}' não é um número inteiro positivo(maior que zero).")
        return obter_numero_intero_faixa(label)

