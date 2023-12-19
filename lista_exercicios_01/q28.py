def  
  caucular_comissao(valor_vendas):
  percentual_comissão = 0.15
  valor_comissão = percentual_comissão * valor_vendas
  return valor_comissao

def
  caucular_salario_final(salario_fixo, valor_comissao)
  salario_final = salario_fixo + valor_comissao
  return salario_final

nome_vendedor = input("Digite o nome do vendedor:")
salario_fixo = float(input("Digite o salário fixo do vendedor:"))
valor_vendas = float(input("Digite o valor total de vendas do vendedor:"))

valor_comissao = caucular_comissao(valor vendas)
salario_final = caucular_salario_final(salario_fixo, valor_comissao)

print("O nome do vendedor é:", nome_vendedor)
print("O salário fixo do vendedor é:", salario_fixo)
print("O valor total de vendas do vendedor é:", valor_vendas)
print("O valor da comissão do vendedor é:", valor_comissao)
print("O salário final do vendedor é:" salario_final)