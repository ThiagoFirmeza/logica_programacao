materia1 = float(input("Digite a nota da matéria 1: "))
materia2 = float(input("Digite a nota da matéria 2: "))
materia3 = float(input("Digite a nota da matéria 3: "))
faltas = int(input("Digite o número de faltas do aluno: "))

frequencia = (30 - faltas) / 30
media = (materia1 + materia2 + materia3) / 3
aprovado = media >= 7 and frequencia >= 0.75

print("Aluno aprovado?", aprovado)