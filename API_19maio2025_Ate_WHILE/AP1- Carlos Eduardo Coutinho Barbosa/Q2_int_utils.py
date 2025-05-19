def num_int_pos():
  num2 = int(input('digite um numero: '))
  if num2 < 0 :
      print('digite um numero positivo!')
  else:
      
      return
      
def num_int():
    num = int(input('digite um numero inteiro: '))
    
    return

def num_int_min():
    x = int(input('determine o valor minimo:'))
    num3 = int(input('digite um numero int: '))
    if num3 <= x:
        print("digite um valor maior que", x)
        
    else:
        
        return
        

def num_int_max():
    x = int(input('determine o limite max: '))
    num4 = int(input('digite um numero menor que: ', x))
    if num4 > x:
        print('digite um numero menor!')
    else:
        
        return            


def num_med():
    lim_max = int(input('determine o limite max:'))
    lim_min = int(input('determine o limite min:'))
    num5 = int(input('digite um numero int entre {lim_max} e {lim_min}: '))
    if num5 < lim_min or num5 > lim_max:
        print("digite um numero entre o limite solicitado")
    else:
        
        return      

num_med()