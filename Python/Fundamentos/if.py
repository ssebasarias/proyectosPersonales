#El operador if busca una condición y, si se cumple, ejecuta un bloque de código.
if True:
  print("Debería ejecutarse")

if False:
  print("Nunca se ejecuta")  
  

pet = input("¿Cuál es tu mascota favorita? ")
if pet == "perro":
  print("Genial, tienes buen gusto")
elif pet == "gato":
  print("Espero tengas suerte")
elif pet == "pez":
  print("Eres lo máximo")
else:
  print("No tienes ninguna mascota interesante")

#El operador elif se utiliza para agregar más condiciones a una declaración if.

'''

stock = int(input("Digita el stock => ")) #Lo que llega del input se transforma directamente a entero

if stock >= 100 and stock <= 1000:
  print("El stock es correcto")
else:
  print("El stock es incorrecto") '''