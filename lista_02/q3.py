tabela = {
    "R": {
        "0-500": 0.40,
        ">500": 0.65
    },
    "C": {
        "0-1000": 0.55,
        ">1000": 0.60
    },
    "I": {
        "0-5000": 0.55,
        ">5000": 0.60
    }}

consumo = float(input("Digite o consumo de kWh: "))
tipo = input("Digite o tipo de instalação (R/C/I): ")

if tipo not in tabela:
    print("Tipo de instalação inválido!")
else:
    faixa = tabela[tipo]
    preco = 0
    for limite, valor in faixa.items():
        if consumo <= limite:
            preco = consumo * valor
            break

print("O preço a pagar é de R$", preco)