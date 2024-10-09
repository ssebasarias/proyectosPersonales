# Leer e imprimir el texto dentro del .txt (linea por linea)
with open('Caperucita.txt', 'r') as file:
    for linea in file:
        print(linea.strip) # Para que tenga en cuenta los saltos de linea se usa el strip

# Leer todas las lineas en una lista 
with open('Caperucita.txt', 'r') as file:
    lines = file.readlines()
    print(lines)

# Añadir texto 
with open('Caperucita.txt', 'a') as file: # a hace referentcia a append
    file.write("\n\nBy: ChatGPT")

# Sobreescribir el texto
with open('Caperucita.txt', 'w') as file: # w es modo escritura y eliminar todo el contenido y reemplazarlo por el que se especifique
    file.write("\n\nBy: ChatGPT")

