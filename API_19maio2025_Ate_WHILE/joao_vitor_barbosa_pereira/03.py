def main():
    num = receberNumfloat()
    numfloat = rebecerfloatNeg()
    numfloatMin = receberfloatmin()
    numfloatmax = receberfloatmax()
    numfloatXY = receberfloatXY()

    print(num)
    print(numfloat)
    print (numfloatMin)
    print(numfloatmax)
    print(numfloatXY)

def receberNumfloat():
    try:
        num = float(input("Escreva um número float: "))
        return num
    except ValueError:
        return receberNumfloat()


def rebecerfloatNeg():
    try:
        num = float(input("Escreva um número float: "))
        if num >= 0:
            return num
        else:
            print("Seu numero é negativo novamente")
            return rebecerfloatNeg()
    except ValueError:
        return rebecerfloatNeg()
    

def receberfloatmin():
    min = float(input("escerva o valor minimo: "))
    try:
        num = float(input("Escreva um número float: "))
        if num > min:
            return num
        else:
            print("tente novamente")
            return receberfloatmin()
    except ValueError:
        return receberfloatmin()

def receberfloatmax():
    max = float(input("escerva o valor maximo: "))
    try:
        num = float(input("Escreva um número float: "))
        if num < max:
            return num
        else:
            print("tente novamente")
            return receberfloatmax()
    except ValueError:
        return receberfloatmax()

def receberfloatXY():
    min = float(input("escerva o valor minimo: "))
    max = float(input("escerva o valor maximo: "))
    try:
        num = float(input("Escreva um número float: "))
        if num < max and num > min:
            return num
        else:
            print("tente novamente")
            return receberfloatXY()
    except ValueError:
        return receberfloatXY()


main()