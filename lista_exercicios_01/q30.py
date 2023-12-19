PI = 3.14159
def 
  caucular_area_triangulo(base, altura):
  area = (base * altura) / 2
  return area

def 
  caucular_area_circulo(raio)
  area = PI * raio ** 2
  return area

def
  caucular_area_trapezio(base_maior, base_menor, altura):
  area =  ((base_maior + base menor) * altura)
  return area

def
  caucular_area_quadrado(lado):
  area = lado ** 2
  return area

def
  caucular_area_retangulo(largura, altura):
  area = largura * altura
  return area

a = float(input(Digite o valor de a:))
b = float(input(Digite o valor de b:))
c = float(input(Digite o valor de c:))

area_triangulo = calcular_area_triangulo(a, c)
area_circulo = calcular_area_circulo(c)
area_trapezio = calcular_area_trapezio(a, b, c)
area_quadrado = calcular_area_quadrado(b)
area_retangulo = calcular_area_retangulo(a, b)

print("A área do trialgulo é:", area_triangulo)
print("A área do circulo é:", area_circulo)
print("A área do trapézio é:", area_trapezio)
print("A área do quadrado é:", area_quadrado)
print("A área do retangulo é:", area_retangulo)

