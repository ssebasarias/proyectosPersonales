squares = [X**2 for X in range(1,11)]
print(squares)

# ejercicio numeros pares
evens = [x for x in range(1,21) if x % 2 == 0]
print('Numero pares: ', evens)

# encontrar la transpuesta de una matris
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

transposed = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
print(matrix)
print(transposed)
