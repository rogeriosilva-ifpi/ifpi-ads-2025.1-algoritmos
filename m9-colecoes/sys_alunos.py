import os
from ulid import ulid

def main():
  alunos = []

  os.system('clear')
  menu = '''
  .... Sys Alunos ...
  1 - Add Aluno
  2 - List Alunos

  0 - Sair 
  
  Opção >>> '''

  opcao = int(input(menu))

  while opcao != 0:

    if opcao == 1:
      novo_aluno = obter_novo_aluno()
      alunos.append(novo_aluno)
      print('Aluno adicionado com sucesso!')
    elif opcao == 2:
      listar_alunos(alunos)

    input('Enter ...')
    os.system('clear')
    opcao = int(input(menu))


def obter_novo_aluno():
  aluno = {}
  aluno['id'] = ulid()
  aluno['nome'] = input('Nome: ')
  aluno['aniversario'] = input('Aniversário (dd/MM): ')
  aluno['clube'] = input('Clube de Futebol: ')

  aluno['sexo'] = input('Sexo [M|F]: ')

  aluno['contatos'] = obter_contatos()


  return aluno


def obter_contatos():
  entrada = input('Contatos (tipo:valor): ')
  itens = entrada.split() #['whatsapp:8688888', ...]

  contatos = []

  for item in itens:
    tipo, valor = item.split(':')
    contato = {
      'tipo': tipo,
      'valor': valor
    }
    contatos.append(contato)

  return contatos




def listar_alunos(alunos):
  print('-----------------')
  for aluno in alunos:
    print(aluno)

  print(10 * '-')


def mapear(colecao, funcao_transformadora):
  nova_colecao = []

  for item in colecao:
    item_transformado = funcao_transformadora(item)
    nova_colecao.append(item_transformado)
  
  return nova_colecao

main()