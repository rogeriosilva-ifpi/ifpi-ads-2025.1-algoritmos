import os
from ulid import ulid
from mfr import filtrar

def main():
  alunos = carregar_alunos_do_arquivo('alunos.txt')

  os.system('clear')
  menu = '''
  .... Sys Alunos ...
  1 - Add Aluno
  2 - List Alunos
  3 - List Aluno por Sexo

  0 - Sair 
  
  Opção >>> '''

  opcao = int(input(menu))

  while opcao != 0:
    if opcao == 1:
      novo_aluno = obter_novo_aluno()
      alunos.append(novo_aluno)
      print('Aluno adicionado com sucesso!')
    elif opcao == 2:
      # ordenados = sorted(alunos, key=por_nome)
      ordenados = sorted(alunos, key=lambda aluno:aluno['nome'])
      listar_alunos(ordenados)
    elif opcao == 3:
      sexo = input('M|F: ')
      alunos_filtrados = filtrar(alunos, lambda aluno:aluno['sexo']==sexo)
      # alunos_filtrados = alunos_por_sexo(alunos, sexo)
      # criterio = por_sexo(sexo)
      # alunos_filtrados = filtrar(alunos, criterio)
      listar_alunos(alunos_filtrados)

    input('Enter ...')
    os.system('clear')
    opcao = int(input(menu))
  

  # sair:
  gravar_dados(alunos, 'alunos.txt')


def por_nome(aluno):
        return aluno['nome']


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
    resultado = f'''
    id: {aluno['id']} - {aluno['nome']} - Sexo: {aluno['sexo']}
      Aniversário: {aluno['aniversario']}.  - Clube: {aluno['clube']}
      Contatos:'''
    print(resultado)
    for contato in aluno['contatos']:
      print(f'\t{contato['tipo']} - {contato['valor']}')
    
  print(10 * '-')


def mapear(colecao, funcao_transformadora):
  nova_colecao = []

  for item in colecao:
    item_transformado = funcao_transformadora(item)
    nova_colecao.append(item_transformado)
  
  return nova_colecao


def carregar_alunos_do_arquivo(nome_arquivo):
  alunos = []
  arquivo = open(nome_arquivo)
  
  for linha in arquivo:
    dados = linha.strip().split('#')
    aluno = {}
    aluno['id'] = dados[0]
    aluno['nome'] = dados[1]
    aluno['aniversario'] = dados[2]
    aluno['clube'] = dados[3]

    aluno['sexo'] = dados[4]

    aluno['contatos'] = []

    contatos = dados[5].split()
    for item in contatos:
      tipo, valor = item.split(':')
      contato = {
        'tipo': tipo,
        'valor': valor
      }
      aluno['contatos'].append(contato)

    alunos.append(aluno)

  return alunos


def gravar_dados(alunos, nome_arquivo):
  #ABCD02#JOAQUINA TERESA#01/08#Fluminense#F#whatsapp:869977-3214
  arquivo = open(nome_arquivo, 'w')

  for aluno in alunos:
    linha_contato = ''
    for contato in aluno['contatos']:
      linha_contato += f'{contato['tipo']}:{contato['valor']} '
    
    linha = f'{aluno['id']}#{aluno['nome']}#{aluno['aniversario']}#{aluno['clube']}#{aluno['sexo']}#{linha_contato}\n'
    arquivo.write(linha)
  
  print('Dados salvos!')


def alunos_por_sexo(alunos, sexo):
  nova_colecao = []

  for aluno in alunos:
    if aluno['sexo'] == sexo:
      nova_colecao.append(aluno)

  return nova_colecao
  

def por_sexo(sexo):

  def inner(aluno):
    return aluno['sexo'] == sexo
  
  return inner


  


main()