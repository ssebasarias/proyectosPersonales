name = "Sebastian"
last_name ="Guerrero"
full_name = name + " " + last_name
print(full_name) #Concatenación de strings

quote = "I'm Lina"
print(quote)

quote2 = 'She said "Hello"'
print(quote2)

#format: Formato de texto
template = "Hola, mi nombre es " + name + " y mi apellido es " + last_name
print('v1', template)

template = "Hola, mi nombre es {} y mi apellido es {}".format(name, last_name) #La función format() permite reemplazar los valores de las llaves por los valores de las variables
print('v2', template)

template = f"Hola, mi nombre es {name} y mi apellido es {last_name}."
print('v3', template)

edad = 25
template2 =f"Tengo {edad} años."
print(template, template2)

#Funciones con strings
text = "Ella sabe programar en Python"
'''
print("JavaScript" in text) # Debe retornar False
print("Python" in text) #Retorna True

if "Python" in text:
  print("Elegiste bien")
else:
 print( "Tambien elegiste bien. Aunque con Pytho puedes trabajar análisis de datos")   
size= len("amor")
print(size)
'''

print("*" * 30)

print(text)
print(len(text)) #la función len() sirve para evaluar el tamaño de un string
print(text.upper()) #Pasa todo a mayusculas
print(text.lower()) #Pasa todo a minusculas
print(text.count('a')) #Cuenta cuantas veces aparece una letra en un string
print(text.swapcase()) #Pasa de mayusculas a minusculas y viceversa
print(text.startswith("Ella")) #Evalua si un string inicia con una palabra en especifico
print(text.endswith("Rust")) #Evalua si un string finaliza con una palabra en especifico
print(text.replace("Python", "Go")) #Reemplaza una palabra por otra

text_2 = "este es un titulo"
print(text_2)
print(text_2.capitalize()) #Pone la primera letra en mayuscula
print(text_2.title()) #Pone la primera letra de cada palabra en mayuscula
print(text_2.isdigit()) #Evalua si un string es un digito
print("398".isdigit())