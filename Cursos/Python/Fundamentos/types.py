'''
Tipos de datos primitivos
Integers: números Enteros
Floats: números de punto flotante (decimales)
Strings: cadena de caracteres (texto)
Boolean: boolenaos (Verdadero o Falso)
Tipos de dato adicionales
Datos en texto: str
Datos numéricos: int, float, complex
Datos en secuencia: list, tuple, range
Datos de mapeo: dict
Set Types: set, frozenset
Datos booleanos: bool
Datos binarios: bytes, bytearray, memoryview '''

#String: Cadena de texto inicializada con comilla doble o comilla simple
my_name = 'Lina'
print('My_name =>', my_name)

print(type(my_name))

#int: Números enteros
my_age = 12
print(my_age,type(my_age)) #Se puede ver el tipo de dato con la función type()

#boolean: Verdadero o Falso
is_single = True
print('is_single =>', is_single)
print(type(is_single))

#inputs: Solicita un valor al usuario
my_age = input('¿Cuál es tu edad? ')
print('my_age =>', my_age)
print(type('my_age'))