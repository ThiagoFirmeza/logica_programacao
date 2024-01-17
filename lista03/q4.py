def decompor(valor):
    notas = []

    while valor >= 100:
        notas.append(100)
        valor -= 100

    while valor >= 50:
        notas.append(50)
        valor -= 50

    while valor >= 20:
        notas.append(20)
        valor -= 20

    while valor >= 10:
        notas.append(10)
        valor -= 10

    while valor >= 5:
        notas.append(5)
        valor -= 5

    while valor >= 2:
        notas.append(2)
        valor -= 2

    while valor >= 1:
        notas.append(1)
        valor -= 1

    return notas

valor = int(input("Digite um valor inteiro: "))

notas = decompor(valor)

print(f"Valor lido: {valor}")
print(f"Relação de notas: {notas}")