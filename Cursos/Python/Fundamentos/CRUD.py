#CRUD: Create, Read, Update & Delete

numbers = [1, 2, 3, 4, 5] #Create
print(numbers[1])
numbers[-1] = 10 #Update
print(numbers) 

numbers.append(700) #Agregar un elemento al final de la lista
print(numbers) 

numbers.insert(0, "hola") #Agregar un elemento en una posición específica
print(numbers)


tasks = ["todo 1", "todo 2", "todo 3"]
new_list = numbers + tasks #Fusionar dos listas
print(new_list)

index = new_list.index("todo 2") #Devuelve 
new_list[index] = "todo changed" #Actualizar un elemento de una lista en la posición que se obttiene con index
print(new_list)

new_list.remove("todo 1") #remueve el elemento que se indique
print(new_list)

new_list.pop() #Elimina el último elemento de la lista
print(new_list)

new_list.pop(0) #Elimina el último elemento de la lista
print(new_list)

new_list.reverse() #Invierte el orden de la lista
print(new_list)

numbers_a = [1, 4, 6, 3]
numbers_a.sort() #Ordena la lista de menor a mayor
print(numbers_a)

strings = ["re", "ab", "ed"]
strings.sort() #Ordena en orden alfabético
print(strings)


#new_list.sort() 
#No se puede ordenar una lista que contiene tipos de datos mezclados