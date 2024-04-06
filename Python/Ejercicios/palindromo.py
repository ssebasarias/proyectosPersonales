def palindromo (palabra):
    palabra = palabra.replace(' ', '')
    palabra = palabra.lower()
    palabra_invertida = palabra[::-1]
    if palabra == palabra_invertida:
        return True
    else:
        return False


# run es el nombre estandar con el cual se nombra la funcion principal (tambien se usa main)
def run ():
    palabra = input('Escribe una palabra: ')
    es_palindromo = palindromo(palabra)
    if es_palindromo == True:
        print('Es palindromo:')
    else:
        print('No es palindromo')


#python ejecuta el programa en el orden en el que aparezca acá
if __name__ == '__main__':
    run ()