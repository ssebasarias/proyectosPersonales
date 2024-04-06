#El operador NOT indica el inverso de un valor booleano.

print(not True)
print(not False)

#Inversión de valores booleanos
print("NOT AND")
print("True and True =>", not ( True and True))
print("True and False =>", not ( True and False))
print("False and True =>", not ( False and True))
print("False and False =>", not ( False and False))

print("*" * 20)

stock = input("Ingrese el número de stock => ")
stock = int(stock)

print(not(stock >= 100 and stock <= 10000))