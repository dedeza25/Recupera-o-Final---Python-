senha_certa = "python123"

while True:
    senha = input("Digite a senha: ")
    if senha == senha_certa:
        print("Acesso permitido")
        break
    else:
        print("Senha incorreta, tente novamente")
