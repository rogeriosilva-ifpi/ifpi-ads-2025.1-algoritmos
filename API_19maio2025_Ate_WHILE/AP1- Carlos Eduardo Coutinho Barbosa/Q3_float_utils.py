def num_int_pos():
  num2 = float(input('digite um numero: '))
  if num2 < 0 :
      print('digite um numero positivo!')
  else:
      
      return
      
def num_int():
    num = float(input('digite um numero inteiro: '))
    
    return

def num_int_min():
    x = float(input('determine o valor minimo:'))
    num3 = float(input('digite um numero float: '))
    if num3 <= x:
        print("digite um valor maior que", x)
        
    else:
        
        return
        

def num_int_max():
    x = float(input('determine o limite max: '))
    num4 = float(input('digite um numero menor que: {x}'))
    if num4 > x:
        print('digite um numero menor!')
    else:
        
        return            


def num_med():
    lim_max = float(input('determine o limite max:'))
    lim_min = float(input('determine o limite min:'))
    num5 = float(input('digite um numero float entre {lim_max} e {lim_min}: '))
    if num5 < lim_min or num5 > lim_max:
        print("digite um numero entre o limite solicitado")
    else:
        
        return        