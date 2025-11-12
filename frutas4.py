try:
    with open("arquivo_inexistente.txt", "r") as arquivo:
        print(arquivo.read())
except FileNotFoundError:
    print("Arquivo não encontrado! Criando um novo arquivo...")
    with open("arquivo_inexistente.txt", "w") as novo:
        novo.write("Arquivo criado automaticamente.\n")
    print("Arquivo criado com sucesso!")