#Diccionarios: Es una estructura de datos que almacena pares clave-valor

my_dict = {} #Creación de un diccionario vacío
print(type(my_dict))


my_dict = {

  "name": "Nicolas",
  "last_name": "Molina Monroy",
  "age": 87,
  "nationality": "Colombian"
}

print(my_dict)

print(len(my_dict)) #Numero de elementos que tiene el diccionario

print(my_dict["age"])
print(my_dict["name"])
print(my_dict.get("Un valor")) #Get se puede usar cuando no se esté seguro de que el valor existe en el diccionario

print("name" in my_dict)
print("otro" in my_dict)

person ={
  "name": "nico",
  "last_name": "molina",
  "langs": ["python", "javascript"],
  "age":30
}

print(person)

#Modificación de elementos
person["name"] = "santi"
person["age"] = 31
person["langs"].append("rust") #Se puede agregar un valor a una lista dentro de un diccionario
print(person)

del person["last_name"] #Elimina un elemento del diccionario


print(person)

person.pop("age") #Elimina un elemento del diccionario
print(person)

print("items") #Genera una dupla de clave y valor de los elementos del diccionario
print(person.items())

print("keys") #Devuelve una lista con los atributos o claves del diccionario
print(person.keys())


print("values") #Devuelve una lista con los valores del diccionario
print(person.values())