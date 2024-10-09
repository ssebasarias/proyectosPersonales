#Tuple: Es una estructura de datos inmutables que contiene una secuencia ordenada de elementos

numbers = (1, 2, 3, 5)
strings = ("nico", "zule", "santi", "nico")
print(numbers)
print("0=>", numbers[0])
print("-1=>", numbers[-1])
print(type(numbers))

print(strings)
print(type(strings))

#A diferencia de las listas, las tuplas no se pueden modificar.

#CRUD 
#numbers.append(10) 
#No se puede agregar un elemento a una tupla
#numbers[1] = "change"

print(strings)
print(strings.index("zule")) #Indice

print(strings.count("nico")) #Función contar cuantas veces aparece un elemento en una tupla

my_list = list(strings) #Convertir una tupla en una lista
print(my_list,type(my_list))

my_list[1] = "juli"
my_tuple = tuple(my_list) #Convertir una lista en una tupla
print(my_tuple)