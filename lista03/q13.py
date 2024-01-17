lista_de_tarefas = []


def adicionar_tarefa(tarefa):
    # Adiciona a tarefa à lista
    lista_de_tarefas.append(tarefa)


def exibir_tarefas():
    # Imprime todas as tarefas
    for tarefa in lista_de_tarefas:
        print(tarefa)


# Exemplo de uso
adicionar_tarefa("Comprar pão")
adicionar_tarefa("Lavar a louça")
adicionar_tarefa("Passar roupa")

exibir_tarefas()