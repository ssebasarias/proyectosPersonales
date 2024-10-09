my_list = [1,2,3,4]

# Obtener iterador
my_iter = iter(my_list)

# Usar iterador
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
# print(next(my_iter)) Este arroja error ya que olo sse puede hacer 4 iteraciones

# Usando bicles
text = 'Hola mundo'
iter_text = iter(text)

for char in iter_text:
    print(char)


# tAMBIEN PUEDEN UARE LO GENERADORES PARA ITERAR
print('GENERATOR')

def my_generator():
    yield 1
    yield 2
    yield 3

for value in my_generator():
    print(value)

# serie de fibonacci
print('fibonacci')
def fibonacci(limit):
    a, b = 0, 1
    while a < limit:
        yield a 
        a , b = b, a+b

for num in fibonacci(10):
    print(num)