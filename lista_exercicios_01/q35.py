def
  calcular_perimetro(lado):
  return 4 * lado


def 
  calcular_area(lado):
  return lado * lado


def
  calcular_diagonal(lado):
  return lado * (2 ** 0.5)

lado = float(input("Digite o valor do lado do quadrado: "))

perimetro = calcular_perimetro(lado)
area = calcular_area(lado)
diagonal = calcular_diagonal(lado)

print("O perímetro do quadrado é de:", perimetro,)
print("A área do quadrado é de:", area,)
print("A diagonal do quadrado é de:", diagonal,)