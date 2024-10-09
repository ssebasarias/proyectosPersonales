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


# manejo del while
x = 0
while x < 5:
  if x == 3:
    break
  # continue
  print(x)
  x += 1