#Ciclos
'''
While True:
  print("Se ejecuta")

counter = 0
while counter < 10:
  counter += 1
  print(counter)
counter = 0

while counter <20:
  counter += 1
  if counter == 15:
    break #Forma forzada de romper un ciclo
  print(counter)
'''
counter = 0

while counter <20:
  counter += 1
  if counter < 15:
    continue #Salta a la siguiente iteración
  print(counter)