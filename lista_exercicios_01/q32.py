def
  caucular_consumo_medio(distancia, combustivel):
  consumo_medio = distancia / combustivel
  return consumo_medio

distancia = float(intup("Digite a distância total percorrida (em km):"))
combustivel = float(input("digite o total de combustivel gasto (em litros):"))

consumo_medio = calcular_consumo_medio(distancia, combustivel)
print("O consumo médio do automóvel é de:", consumo_medio, "km/l")