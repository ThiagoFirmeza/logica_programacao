def
  calcular_litros_gasto(tempo, velocidade):
  distancia = tempo * velocidade
  litros_gasto = distancia / 12
  return litros_gasto

tempo = float(input("Digite o tempo gasto na viagem (em horas): "))
velocidade = float(input("Digite a velocidade média durante a viagem (em km/h): "))

litros_gasto = calcular_litros_gasto(tempo, velocidade)
print("A quantidade de litros de combustível gastos é de:", litros_gasto, "litros")
