def
  caucular_media_ponderada 
  (nota1: int); (nota2: int); (nota3: int) 
   peso1 = 2
   peso2 = 3
   peso3 = 5 

 media_ponderada = (nota1 * peso1 + nota2 * peso2 + nota3 * peso3) / (peso1 + peso2 + peso3)
 return media_ponderada

 nota1 = int(input("Digite a nota 1:"))
 nota2 = int(input("Digite a nota 2:"))
 nota3 = int(input("Digite a nota 3:"))

 media_ponderada = calcular_media_ponderada(nota1, nota2, nota3)

 print("A média ponderada do aluno é:", media_ponderada)