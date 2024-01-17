#questão 01 letra A
for i in range(1, 101):
    print(i)

#questão 01 letra B
for i in range(50, 101, 2):
    print(i)

#questão 01 letra C
for i in range(10, 0, -1):
    print(i)
print("Fogo!")

#questão 01 letra D
limite = int(input("Digite o valor limite:"))
tipo = str(input("Deseja imprimir os pares (P) ou ímpares (I)? "))

if tipo == "p":
    for i in range(1, limite + 1):
        if i % 2 == 0:
            print(i)
elif tipo == "i":
    for i in range(1, limite + 1):
        if i % 2 != 0:
            print(i)
else:
    print("Opção inválida!")