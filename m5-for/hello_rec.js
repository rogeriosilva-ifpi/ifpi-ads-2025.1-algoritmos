import { question } from 'readline-sync'

function main(){
  const nome = question('Qual seu nome: ')
  const qtd = Number(question('Quer ver seu nome quantas vezes? '))
  
  // C-Like FOR, FOR de 3 expressões(init, condicao, increment/converge)
  escrever_nome(nome, qtd)

  console.log('Fim.')
}

function escrever_nome(nome, qtd){
  if (qtd === 0){
    return
  }
  console.log(nome)
  escrever_nome(nome, qtd-1)
}

main()