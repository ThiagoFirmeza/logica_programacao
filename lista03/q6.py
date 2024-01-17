def contem_item(lista, item):
    return item in lista


def junta_listas_sem_repetidos(lista1, lista2):
    lista_resultado = []

    for item in lista1:
        if not contem_item(lista_resultado, item):
            lista_resultado.append(item)

    for item in lista2:
        if not contem_item(lista_resultado, item):
            lista_resultado.append(item)

    return lista_resultado


lista1 = [1, 2, 3, 4, 5]
lista2 = [6, 7, 8, 9, 10]

lista_resultado = junta_listas_sem_repetidos(lista1, lista2)

print(lista_resultado)