def 
  caucular_sálario(matricula, horas_trabalhadas, valor_hora)
  salario = horas_trabalhadas * valor_hora
  return salário

matricula = input("Digite o número da matricula do funcionário:")
horas_trabalhadas = int(input("Digite o número de horas trabalhadas:"))
valor_hora = float(input("Digite o valor recebido por hora:"))

 salario = calcular_salario(matricula, horas_trabalhadas, valor_hora)
print("A matricula do funcionário é:", matricula)
print("O salário do funcionário é:", salário)

