def conversor(tipo_pesos, valor_dolar):
    pesos = input("¿Cuantos pesos" + tipo_pesos +"tienes?: ")
    pesos = float(pesos)
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes $" + dolares + " dólares")

menu = """
Bienvenido al conversor de monedas 💰

1 - Pesos bolivianos
2 - Pesos colombianos
3 - Pesos argentinos
4 - Pesos mexicanos

Elige una opción: """

opcion = int(input(menu))

if opcion == 1:
    conversor("bolivianos", 6.90)
elif opcion == 2:
    conversor("colombianos", 3.73)
elif opcion == 3:
    conversor("argentinos", 4.22)
elif opcion == 4:
    conversor("mexicanos", 19.88)
else:
    print("Ingrese una opción correcta por favor")