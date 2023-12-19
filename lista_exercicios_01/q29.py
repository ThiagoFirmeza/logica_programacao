PI = 3.14159
def 
  caucular_volume_esfera(raio):
  volume = (4 / 3) * PI * raio ** 3
  return volume

raio = float(input("Digite o raio da esfera:"))
volume = caucular_volume_esfera(raio)
print("O volume da esfera é:", volume)
