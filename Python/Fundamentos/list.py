#Listas: Conjunto de datos

numbers = [1, 2, 3, 4]
print(numbers)
print(type(numbers))

tasks = ["make a dishes", "play videogames"]
print(tasks)

types = [1, True, "hola"]
print(types)

print(numbers[0]) #Se retorna el numero que se indique dentro de []
print(tasks[0])
''' text = "Hola"
text[0] "W"''' #No se puede modificar un string como una lista

tasks[0] ="watch platzi courses" #Se puede modificar un elemento de una lista
print(tasks)

tasks[0] = "do the dishes"
print(tasks)

print(numbers[:3]) #Se puede seleccionar un rango de elementos de una lista

print(True in types)
print("hola" in types)