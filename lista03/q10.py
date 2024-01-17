#quetsão 10 letra A
def area_quadrado(lado, exibir=False):
    area = lado * lado
    if exibir:
        print(f"A área do quadrado é {area}")
    return area

#questão 10 letra B
def area_triângulo(base, altura, exibir=False):
    area = (base * altura) / 2
    if exibir:
        print(f"A área do triângulo é {area}")
    return area
