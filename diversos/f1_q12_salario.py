# 12. Leia o salário de um trabalhador e 
# escreva seu novo salário com um aumento de 25%.

# entrada
salario = float(input('Salário: '))

# processamento
# aumento = (salario / 100) * 25
aumento = salario * (25/100)
novo_salario = salario + aumento #snake_case

# saida
print(f'Seu salário era R$ {salario:.2f}')
print(f'E aumentará 25%, ou seja, R$ {aumento:.2f}')
print(f'Então, seu novo salário será de R$ {novo_salario:.2f}')