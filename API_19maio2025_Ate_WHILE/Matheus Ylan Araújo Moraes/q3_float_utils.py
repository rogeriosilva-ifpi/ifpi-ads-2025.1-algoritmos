def main():
    def obter_numero_real(label):
        valor = input(label)
        try:
            numero = float(valor)
            return numero
        except ValueError:
            print(f"O valor que você passou '{valor}' não é um número real")
            return obter_numero_real(label)
        
    num_real = obter_numero_real("Insira um número real valido: ")

    print(f"Seu número real é {num_real}.")
    print("Fim.")

main()