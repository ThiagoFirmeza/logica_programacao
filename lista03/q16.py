contatos = []

def adicionar_contato():
    nome = input("Nome: ")
    telefone = input("Telefone: ")
    contato = {"nome": nome, "telefone": telefone}
    contatos.append(contato)

def buscar_contato():
    nome = input("Nome: ")
    for contato in contatos:
        if contato["nome"] == nome:
            print(contato["telefone"])
            return
    print("O contato não foi encontrado")

def sair():
    print("Saindo do programa...")

while True:
    print("1. Adicionar contato")
    print("2. Buscar contato")
    print("3. Sair")

    opcao = int(input("Opção: "))

    if opcao == 1:
        adicionar_contato()
    elif opcao == 2:
        buscar_contato()
    elif opcao == 3:
        sair()
        break