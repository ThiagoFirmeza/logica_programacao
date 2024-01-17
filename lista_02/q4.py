distancia = float(input("Digite a distância que deseja percorrer em km: "))

if distancia <= 200:
    preco = distancia * 0.5
else:
    preco = distancia * 0.45

print("O preço da passagem é de R$", preco)