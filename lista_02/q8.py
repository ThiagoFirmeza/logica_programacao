hora_inicial = int(input("Digite a hora inicial do jogo: "))
minuto_inicial = int(input("Digite o minuto inicial do jogo: "))
hora_final = int(input("Digite a hora final do jogo: "))
minuto_final = int(input("Digite o minuto final do jogo: "))

if hora_inicial > hora_final:
    print("Hora inicial não pode ser maior que a hora final!")
elif minuto_inicial > minuto_final:
    print("Minuto inicial não pode ser maior que o minuto final!")
elif hora_inicial == hora_final and minuto_inicial == minuto_final:
    print("O jogo durou 0 minuto(s).")
else:
    duracao_minutos = minuto_final - minuto_inicial
    duracao_horas = hora_final - hora_inicial
if duracao_minutos < 0:
        duracao_minutos += 60
        duracao_horas -= 1
    duracao_total = duracao_horas * 60 + duracao_minutos
    print("O jogo durou", duracao_total, "minuto(s).")