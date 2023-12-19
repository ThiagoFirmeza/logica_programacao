def
  calcular_resultado(a, b, c, d):
   return a > b and c or not d


resultado_1 = calcular_resultado(1, 2, True, False)
resultado_2 = calcular_resultado(10, 3, False, True)
resultado_3 = calcular_resultado(5, 1, True, True)

print("Resultado 1:", resultado_1)
print("Resultado 2:", resultado_2)
print("Resultado 3:", resultado_3)