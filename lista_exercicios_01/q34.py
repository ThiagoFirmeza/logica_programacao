def 
  calcular_total_segundos(dias, horas, minutos, segundos):
  total_segundos = dias * 86400 + horas * 3600 + minutos * 60 + segundos
  return total_segundos

dias = int(input("Digite a quantidade de dias: "))
horas = int(input("Digite a quantidade de horas: "))
minutos = int(input("Digite a quantidade de minutos: "))
segundos = int(input("Digite a quantidade de segundos: "))

total_segundos = calcular_total_segundos(dias, horas, minutos, segundos)
print("O total em segundos é de:", total_segundos)