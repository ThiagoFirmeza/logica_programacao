def verifica_parenteses(expressao):
    pilha = []

    for caractere in expressao:
        if caractere == "(":
            pilha.append(caractere)
        elif caractere == ")":
            if len(pilha) == 0:
                return False
            else:
                pilha.pop()
    return len(pilha) == 0


expressao = input("Digite uma expressão com parênteses: ")

if verifica_parenteses(expressao):
    print("Os parênteses estão balanceados.")
else:
    print("Os parênteses não estão balanceados.")