
def main():
    somatorio = 0
    while True:
      animal = input('Insira um animal com 7 letras ou mais > ')
      if len(animal) < 7:
         print('Ele nao tem 7 letras ou mais.')
         input('Aperte ENTER para tentar novamente.')
      else:
         i = 0
         while i < len(animal):
           int_quant = int(input('Insira um número > '))
           
           somatorio += int_quant
           i += 1  
         media = somatorio / len(animal)
         print(f"""
-----------------------------
         MÉDIA > {media:.2f}
         SOMATÓRIO > {somatorio}
-----------------------------------
""")
         break



main()