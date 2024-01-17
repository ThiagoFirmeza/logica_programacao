import random

numero_secreto = random.randint(1, 100)

palpite = 0

while palpite != numero_secreto:

palpite = int(input("Tente adivinhar o número secreto: "))

    if palpite > numero_secreto:
        print("Tente um número menor.")
    elif palpite < numero_secreto:
        print("Tente um número maior.")

print("Parabéns!! Você acertou o número secreto:", numero_secreto)