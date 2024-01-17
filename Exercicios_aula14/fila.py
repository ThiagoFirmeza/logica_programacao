fila = list(range(1, 11))
tamanho_fila = len(fila)

while True:
    print("Escolha uma opção:")
    print("F - Adicionar uma pessoa a fila")
    print("A - Atender uma pessoa")
    print("S - Sair")

    opção = input()

    if opção == "F":
        tamanho_fila += 1
        fila.append(tamanho_fila)
        print("Fila:", fila)
        print("Tamanho da fila:", tamanho_fila)

    elif opção == "A":
        fila.pop(0)
        tamanho_fila -= 1
        print("Fila:", fila)
        print("Tamanho da fila:", tamanho_fila)

    elif opção == "S":
        break

    else:
        print("Opção invalida")
