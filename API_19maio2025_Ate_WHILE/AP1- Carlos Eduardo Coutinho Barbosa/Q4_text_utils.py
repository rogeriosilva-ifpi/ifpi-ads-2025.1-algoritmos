def get_text():
    text = float(input('digite seu texto: '))
    text = str
    return

def get_text_min():
    min_text = float(input('determine o valor minimo de chars:'))
    text2 = float(input('digite o seu texto: '))
    text2 = str
    if text2 < min_text:
        print("digite um texto com mais chars que", min_text)
        
    else:
        
        return

def get_text_max_min():
    lim_max = float(input('determine o limite max:'))
    lim_min = float(input('determine o limite min:'))
    text4 = float(input('digite um texto com chars entre {lim_max} e {lim_min}: '))
    text4 = str
    if text4 < lim_min or text4 > lim_max:
        print("digite um texto entre o limite solicitado")
    else:
        
        return        