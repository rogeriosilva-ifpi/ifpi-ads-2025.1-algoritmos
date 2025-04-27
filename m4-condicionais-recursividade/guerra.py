def main():
  print('Hello War!!!')
  ano_nascimento = int(input('Ano Nasc.: '))
  idade = 2025 - ano_nascimento

  print(f'Você tem {idade} anos')

  if eh_maior_idade(idade) and not eh_idoso(idade):
    print('Você foi convocado!')
  else:
    print('Fique em casa orando!')  

  print('Fim...')

def eh_maior_idade(idade: int):
  return idade >= 18
  

def eh_idoso(idade: int):
  return idade >= 60


main()