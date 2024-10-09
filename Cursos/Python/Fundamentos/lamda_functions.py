# 
add = lambda a, b: a + b
print(add(10, 4)) 

# Cuadrado de numero 
number = range(11)
squared_numbers = list(map(lambda x: x**2, number)) # map() itera la funcionn por cada elemneto
print('Cuadrados: ', squared_numbers)

# pares
even_numbers = list(filter(lambda x: x%2 == 0, number)) # filter() filtra cada elemento iterable a travez de una funcion
print('Pares: ', even_numbers)