#Loops: Ciclos

matriz = [
  [1,2,3], 
  [4,5,6], 
  [7,8,9]
]

print(matriz[0])

print(matriz[0][1]) #Orden de filas y columnas

for row in matriz:
  print(row)
  for column in row:
    print(column)