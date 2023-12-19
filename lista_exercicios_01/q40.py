resultado_1 = 3 < 2 ** 3 and 3 == 3 
# Ordem de execução:
# 2 ** 3 = 8
# 3 < 8 = False
# 3 == 3 = True
# False and True = False

resultado_2 =  0 != 4 or (3/3 == 1 and (5 + 1) / 3 == 2)
# Ordem de execução:
# 0 != 4 = True
# 3/3 == 1 = True
# (5 + 1) / 3 == 2 = True
# True or True = True