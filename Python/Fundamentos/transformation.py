name = "Lina"
print(type(name))
name = 12
print(type(name))
name = True
print(type(name))

print("Lina" + " " + "Ospina") # Concatena
print(10 + 20) #suma

#print("Lina" + 12) # No se puede concatenar un string con un entero

print("Lina" + "12") #Si se puede concatenar un string con un string

age = 12
print("Mi edad es " + str(age)) # La función str() transforma el tipo de dato de un entero a string
print(f"Mi edad es {age}") #La función f"{}" transforma el tipo de dato de un entero a string

age = input("Escribe tu edad => ")
print(type(age))
age =int(age) # La función int() transforma el tipo de dato de un string a entero
age += 10
print(type(age))
print(f'Tu edad en 10 años será {age}')