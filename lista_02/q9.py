import random

opcoes = ["pedra", "papel", "tesoura"]
opcao_computador = random.randint(0, 2)
opcao_jogador = input("Escolha uma opção: pedra, papel ou tesoura: ")

if opcao_jogador == opcoes[opcao_computador]:
    print("Empate!")
elif opcao_jogador == "pedra" and opcao_computador == "tesoura":
    print("Jogador venceu!")
elif opcao_jogador == "papel" and opcao_computador == "pedra":
    print("Jogador venceu!")
elif opcao_jogador == "tesoura" and opcao_computador == "papel":
    print("Jogador venceu!")
else:
    print("Computador venceu!")