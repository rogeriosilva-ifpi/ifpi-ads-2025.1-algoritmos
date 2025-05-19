def main():
    num = receberNumInt()
    numint = rebecerIntNeg()
    numintMin = receberintmin()
    numintmax = receberintmax()
    numintXY = receberintXY()

    print(num)
    print(numint)
    print (numintMin)
    print(numintmax)
    print(numintXY)

def receberNumInt():
    try:
        num = int(input("Escreva um número inteiro: "))
        return num
    except ValueError:
        return receberNumInt()


def rebecerIntNeg():
    try:
        num = int(input("Escreva um número inteiro: "))
        if num >= 0:
            return num
        else:
            print("Seu numero é negativo novamente")
            return rebecerIntNeg()
    except ValueError:
        return rebecerIntNeg()
    

def receberintmin():
    min = int(input("escerva o valor min: "))
    try:
        num = int(input("Escreva um número inteiro: "))
        if num > min:
            return num
        else:
            print("tente novamente")
            return receberintmin()
    except ValueError:
        return receberintmin()

def receberintmax():
    max = int(input("escerva o valor maximo: "))
    try:
        num = int(input("Escreva um número inteiro: "))
        if num < max:
            return num
        else:
            print("tente novamente")
            return receberintmax()
    except ValueError:
        return receberintmax()

def receberintXY():
    min = float(input("escerva o valor minimo: "))
    max = float(input("escerva o valor maximo: "))
    try:
        num = int(input("Escreva um número inteiro: "))
        if num < max and num > min:
            return num
        else:
            print("tente novamente")
            return receberintXY()
    except ValueError:
        return receberintXY()


main()