def gritar_feliz_natal(felicidade):
    if felicidade <= 1:
        raise ValueError("A felicidade deve ser maior que 1")
    grito = "Feliz Natal!!"
    for i in range(felicidade - 1):
        grito += "!!!"
    return grito

print(gritar_feliz_natal(2))
print(gritar_feliz_natal(5))
