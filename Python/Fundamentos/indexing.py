text = "Ella sabe Python"
print(text[0]) #Retorna el caracter en la posición 0
size = len(text)
print(text[size - 1]) #Retorna el último caracter del string
print(text[-1]) #Retorna el último caracter del string


# Slicing
print(text[0:5]) #Retorna los caracteres desde la posición 0 a la 5

print(text[10:16])
print(text[:10]) #Si no se indica el inicio, se toma por defecto el inicio en 0
print(text[5:-1])
print(text[:]) #Retorna todo el string
print(text[10:16:1]) #Retorna los caracteres desde la posición 10 a la 16
print(text[10:16:2]) #Retorna los caracteres desde la posición 10 a la 16 saltando de a 2
print(text[::2]) #Retorna los caracteres desde la posición 0 a la 16, saltando de a 2 caracteres