#RETO ANTES DE VER LA CLASE

# def potencia (num, limit):
#     count = 1
#     result = num
#     while count < limit:
#         result = result * num
#         count += 1
#         print (count)
#     return result

# numero = 2
# limite = 100

# print(potencia(numero, limite))

#_______ WHILE _________

def potencia(numero, limite):
    
    potencia = 1

    while (potencia <= limite):
        
        result = numero ** potencia
        print('Potencia de {} elevado a la {} es {}'.format(numero, potencia, result))
        potencia += 1
        

def run():
    numero = int(input('Escribe el numero al cual quieres averiguarle la potencia: '))
    limite = int(input('Escribe el potencia: '))
    potencia(numero, limite)


if __name__ == "__main__":
    run()


#_______ FOR _________

def tabla(numero):
    print('Esta es la tabla del ' + str(numero))
    for i in range(1,10 +1):
        print(i*numero)


def run():
    menu = """
VAMOS A VISUALIZAR LAS TABLAS DE MULTIPLICAR
    Selecciona la tabla que quieras ver:
        a. tabla del 2
        b. tabla del 3
        c. tabla del 4
        d. tabla del 5
        e. tabla del 6
        f. tabla del 7
        g. tabla del 8
        h. tabla del 9
            
¿Qué tabla quires ver? Elige una opcion: 
    """
    opcion = str(input(menu))

    if opcion == 'a':
        tabla(2)
    elif opcion == 'b':
        tabla(3)
    elif opcion == 'c':
        tabla(4)
    elif opcion == 'd':
        tabla(5)
    elif opcion == 'e':
        tabla(6)
    elif opcion == 'f':
        tabla(7)
    elif opcion == 'g':
        tabla(8)   
    elif opcion == 'h':
        tabla(9)                         
    else:
        print('esa no es una opcion')


if __name__ == '__main__':
    run()

#vgy