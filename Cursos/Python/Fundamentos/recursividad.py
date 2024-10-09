# Factoriales
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
    
result_factorial = factorial(5)
print('Factorial: ', result_factorial)

# Fibonacci
def fibonacci(n): 
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
result_fibonacci = fibonacci(6)
print('Fibonacci: ', result_fibonacci)