#Operadores lógicos
#AND: El operador and devuelve True si ambos operandos son True.
print("Tabla de operadores lógicos")
print("True and True =>", True and True)
print("True and False =>", True and False)
print("False and True =>", False and True)
print("False and False =>", False and False)

print("*" * 20)
print(10>5 and 5<10) #Se cumple la condición de ambos operadores
print(10>5 and 5>10)

print("*" * 20)

stock = input("Ingrese el número de stock => ")
stock = int(stock)

print(stock >= 100 and stock <= 10000)

print("*" * 20)

#OR: El operador or devuelve True si al menos uno de los operandos es True.
print("Tabla de operadores lógicos")
print("True or True =>", True or True)
print("True or False =>", True or False)
print("False or True =>", False or True)
print("False or False =>", False or False)

print("*" * 20)

role = input("Digita el rol => ")
print(role == "admin" or role == "seller")