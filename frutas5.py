nome = input("Digite seu nome: ")
email = input("Digite seu e-mail: ")

with open("usuarios.txt", "a") as arquivo:
    arquivo.write(f"Nome: {nome} | Email: {email}\n")

print("Usuário cadastrado com sucesso!")