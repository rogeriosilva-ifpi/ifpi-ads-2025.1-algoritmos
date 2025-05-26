def main():
    # Inválida por usar recursos nao estudados até o momento
    print(calculo_com_nome("dois"))
    print(calculo_com_nome("cinco"))

def calculo_com_nome(nome: str) -> list[int]:
    comprimento_nome = len(nome)
    if comprimento_nome % 2 != 0:
        divisores = []
        possivel_divisor = comprimento_nome
        while possivel_divisor > 0 :
            if comprimento_nome % possivel_divisor == 0:
                divisores.append(possivel_divisor)
            possivel_divisor -= 1
        return divisores        
    else:
        multiplo = 1
        multiplos = []
        while multiplo <= comprimento_nome:
            multiplos.append(multiplo * comprimento_nome)
            multiplo += 1
        return multiplos


main()