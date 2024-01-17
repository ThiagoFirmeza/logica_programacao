#questão 02 letra A
def multiplicacao(a, b):
    resultado = 0
    while b > 0:
        resultado += a
        b -= 1
    return resultado


a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))

print(f"A multiplicação de {a} por {b} é: {multiplicacao(a, b)}")

#questão 02 letra B
def divisao(a, b):
    resto = a
    quociente = 0
    while resto >= b:
        resto -= b
        quociente += 1
    return quociente, resto


a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))

quociente, resto = divisao(a, b)

print(f"A divisão de {a} por {b} é: {quociente} com resto {resto}")