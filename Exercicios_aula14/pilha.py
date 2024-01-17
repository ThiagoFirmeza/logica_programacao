pilha = list(range(1, 6))
tamanho_pilha = len(pilha)

while True:
    print("Escolha uma opção:")
    print("E - Colocar um novo prato")
    print("D - Remover um proto da pilha")
    print("S - Sair")

    opção = input()

    if opção == "E":
        tamanho_pilha +=1
        pilha.append(tamanho_pilha)
        print("Pilha:", pilha)
        print("Tamanho_pilha:", tamanho_pilha)
    
    elif opção == "D":
        pilha.pop(0)
        tamanho_pilha -= 1
        print("Pilha:", pilha)
        print("Tamanho da pilha:", tamanho_pilha)

    elif opção == "S":
        break

    else:
        print("Opção invalida")