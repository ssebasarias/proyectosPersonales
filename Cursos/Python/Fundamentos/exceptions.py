try: 
    divisor = int(input('Ingrese el divisor: '))
    result = 100 / divisor
    print('Resultado: ', result) 
except ZeroDivisionError as e:
    print('El divior debe er mayor a cero')
except ValueError as e:
    print('Ha ocurrido un error: ', e)
    print('Debes introducir un numero valido')

