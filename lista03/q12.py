def contagem_regressiva(n):
    if n <= 0:
        print("Bum!")
    else:
        print(n)
        contagem_regressiva(n - 1)


n = int(input("Digite um número inteiro: "))
contagem_regressiva(n)