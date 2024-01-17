a = float(input("Digite o valor de A: "))
b = float(input("Digite o valor de B: "))
c = float(input("Digite o valor de C: "))

if a <= b:
    a, b = b, a
if a <= c:
    a, c = c, a

if a >= b + c:
    print("NAO FORMA TRIANGULO")
elif a ** 2 == b ** 2 + c ** 2:
    print("TRIANGULO RETANGULO")
elif a ** 2 > b ** 2 + c ** 2:
    print("TRIANGULO OBTUSANGULO")
elif a ** 2 < b ** 2 + c ** 2:
    print("TRIANGULO ACUTANGULO")
elif a == b == c:
    print("TRIANGULO EQUILATERO")
else:
    print("TRIANGULO ISOSCELES")