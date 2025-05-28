import { question } from 'readline-sync'

function main(){
  const nome = question('Qual seu nome: ')
  const qtd = Number(question('Quer ver seu nome quantas vezes? '))
  
  // C-Like FOR, FOR de 3 expressões(init, condicao, increment/converge)
  for(let i = 0; i < qtd; i++){
    console.log(`${i} >> Olá ${nome}!`)
  }

  console.log('Fim.')
}

main()