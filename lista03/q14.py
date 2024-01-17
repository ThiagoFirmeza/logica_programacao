#passagem por valor
def dobrar(valor):
    # A função recebe uma cópia do valor de 'numero'
    valor *= 2


numero = 10

# O valor de 'numero' não é alterado
print(numero)

# A função dobra o valor de 'numero'
dobrar(numero)

# O valor de 'numero' ainda não é alterado
print(numero)

#passagem por referência
def dobrar(numero):
    # A função recebe a referência para 'numero'
    numero *= 2


numero = 10

# O valor de 'numero' é alterado
print(numero)

# A função dobra o valor de 'numero'
dobrar(numero)

# O valor de 'numero' é alterado
print(numero)