'''

#For: ciclos que se repiten un número determinado de veces. 
#Ciclos definidos

for element in range(20): #La función range entrega una lista de números desde 0 hasta el número que se indique.
 
  print(element)

print("*" * 30)

my_list = [23, 45, 67, 89, 43]
for element in my_list:
  print(element)

print("*" * 30)

my_tuple = ("nico", "juli", "santi")
for element in my_tuple:
  print(element)

print("*" * 30)

product = {
  "name": "camisa",
  "price": 100,
  "stock": 89
}

for key in product:
  print(key, "=>", product[key])

print("*" * 30)

for key, value in product.items(): #Value es el valor del elemento
  print(key, "=>", value)

print("*" * 30)


#Lista de diccionarios
people = [
  {
    "name": "nico",
    "age": 34
  },
  {
    "name": "zule",
    "age": 45
  },
  {
    "name": "santi",
    "age": 4
  }
]

for person in people:
  print("name =>", person["name"])


for i in range(1,11):
  print(i**2)'''

n = [i**2 for i in range(1,11)]
print(n)