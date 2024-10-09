x = 3.3
print(x)
y = 1.1 + 2.2
print(y)
print(x == y) #Comparación de flotantes

y_str = format(y, ".2g") #La función .númerog, toma el número de dígitos que se le indique y lo redondea.
print("str =>", y_str)

print(y_str == str(x)) #Se escribe la variable en formato string para poder compararla con la variable x

print("*" * 20)#Segunda forma

print(x,y)
tolerance = 0.00001
print(abs(x - y) < tolerance) 
#Se usa la función abs para obtener el valor absoluto de la resta de x y y, para compararlo con la tolerancia establecida.