def usuario():
    nome = input('Ecreva seu nome: ')
    count = 0
    soma = len(nome)
    divisores = len(nome)

    while nome == nome:
        if len(nome) % 2 == 0:
            while count <= len(nome):    
                print(f'Os multiplos de {len(nome)} são: {soma}')
                soma += len(nome)
                count += 1
            break
        else:
            while divisores > 0:
                print(f'Os divisores de {len(nome)} são: {divisores}')
                divisores = len(nome) / len(nome) - 1
                divisores -= 1
            break
usuario()   