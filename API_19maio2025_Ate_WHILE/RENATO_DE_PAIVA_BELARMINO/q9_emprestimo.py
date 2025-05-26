

def main():
    renda_mensal = float(input('Insira sua renda mensal > '))
    
    while True:
      valor_emprestimo = float(input('Insira o valor do empréstimo > '))
      if valor_emprestimo >= 1518:
          break
      else:
          print('Empréstimo deve custar no mínimo 1 salário mínimo (R$ 1518)')
          input('Aperte ENTER para tentar novamente.')

    while True:
      prazo = int(input('Qual o prazo desejado? (meses) > '))
      if prazo <= 24 and prazo >= 2:
         break
      elif prazo > 24:
         print('O prazo deve ser de no máximo 24 meses.')
         input('Aperte ENTER para tentar novamente.')
         continue
      else:
         print('O prazo deve ser de no mínimo 2 meses.')
         input('Aperte ENTER para tentar novamente.')
    resultado(renda_mensal, valor_emprestimo, prazo)




def resultado(renda_mensal, valor_emprestimo, prazo):
    selic = 14.75
    prazo_dias = prazo * 30
    iof = valor_emprestimo * 0.0038 + (prazo_dias * 0.000082)
    if prazo >= 6:
         juros = ((valor_emprestimo + iof) / prazo) * (selic * 0.5)
    elif prazo >= 12:
         jjuros = ((valor_emprestimo + iof) / prazo) * (selic * 0.75)
    elif prazo >= 18:
         juros = ((valor_emprestimo + iof) / prazo) * (selic)
    else:
       juros = ((valor_emprestimo + iof) / prazo) * (selic * 1.3)
    total = juros + valor_emprestimo + iof
    parcela_mensal = total / prazo
    if parcela_mensal <= (renda_mensal * 0.3):
       emprestimo = 'APROVADO.'
    else:
       emprestimo = 'NEGADO.'
    print(f"""
-----------------------
          IOF: R$ {iof:.2f}
          JUROS: R$ {juros:.2f}
          VALOR TOTAL A PAGAR: R$ {total:.2f}
          VALOR DA PARCELA MENSAL: R$ {parcela_mensal:.2f}
          Empréstimo: {emprestimo}
---------------------------------------------
""")
    

main()