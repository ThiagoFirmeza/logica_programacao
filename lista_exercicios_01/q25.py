def 
  caucular_diferenca(a, b, c, d)
  diferenca = (a * b - c * d)
  return diferenca

a = int(input("Digite o valor de a:"))
b = int(input("digite o valor de b:"))
c = int(input("digite o valor de c:"))
d = int(input("digite o valor de d:"))

diferenca = caucular_diferenca(a, b, c, d)
print("A diferença é:", diferenca)

#Os parênteses são necessário sim, pois sem os parênteses, a operação de subtração será realizada primeiro.