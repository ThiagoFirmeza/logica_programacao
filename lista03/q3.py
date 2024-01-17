numeros = []

while True:
    numero = int(input("Digite um número: "))
    if numero == 0:
        break
    numeros.append(numero)

quantidade = len(numeros)
soma = sum(numeros)

print(f"Quantidade de números: {quantidade}")
print(f"Soma dos números: {soma}")
print(f"Média aritmética: {media}")