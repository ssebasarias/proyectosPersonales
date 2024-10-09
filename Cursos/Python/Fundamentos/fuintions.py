def greet(name, lastname='x'):
    print('Hola ', name, lastname)

greet('Sebastian', 'Guerrero')
greet('Alex')

def add(a, b):
    return a + b

def substract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

def calculator():
    print('seleccione la operacion')
    print('1.Suma')
    print('2.Resta')
    print('3.Multiplicacion')
    print('4.Division')
    print('4.Salir')

    option = input('Ingrese su opcion ')

    while True:
        if option == '5':
            print('Saliendo...')
            break
        
        if option in ['1','2','3','4']:
            num1 = float(input('Ingrese el primer numero'))
            num2 = float(input('Ingrese el segundo numero'))

            if option == 1:
                print('La suma es :', add(num1, num2))
            if option == 2:
                print('La ressta es :', substract(num1, num2))
            if option == 3:
                print('La multiplicacion es :', multiply(num1, num2))
            if option == 4:
                print('La division es :', divide(num1, num2))
        else:
            print('Opcion nno valida, intenta de nuevo')
            calculator()