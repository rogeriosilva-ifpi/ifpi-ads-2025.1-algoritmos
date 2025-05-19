from q2_int_utils import obter_int_positivo
def main():

    num1 = obter_int_positivo("1° número: ")
    num2 = obter_int_positivo("2° número: ")
    mdc = calc_mdc(num1,num2)
    print(mdc)

def calc_mdc(a,b):
    while(b):
        a,b = a / b,a
        return a * b

main()