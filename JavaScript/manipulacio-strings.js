//String primitivo
const stringPrimitivo = 'soy un string primitivo'
console.log(typeof stringPrimitivo)

const stringPrimitivoTambien = String('Soy un string primitivo también')
console.log(typeof stringPrimitivoTambien)

//String Objeto
const stringObjeto = new String('Soy un string objeto')
console.log(typeof stringObjeto)

//Acceder a caracteres
const saludo = 'Hola. ¿Cómo estás?'

//Acceder a una letra por su índice.
console.log(saludo[2])
console.log(saludo.charAt(2))

//conocer el indice de una letra
console.log(saludo.indexOf('o'))

//Conocer dónde inicia una palabra
console.log(saludo.indexOf('Cómo'))

//Conocer si existe una palabra dentro de un texto, en caso de no existir se devolverá -1.
console.log(saludo.indexOf('como'))

//Conocer la última posición de una letra
console.log(saludo.lastIndexOf('o'))

//Extraer letras entre un determinado rango. Ingresar el índice inicial y el final más 1.
console.log(saludo.slice(3,5))

//conocer la longitud de un string
console.log(saludo.length)

//Colocar todo el texto en mayúscula
console.log(saludo.toUpperCase())

//Colocar todo el texto en minúscula
console.log(saludo.toLocaleLowerCase())

//Dividir un string. Con el método split colocar la forma como se quiere dividir en medio de las comillas.
const saludoDividido = saludo.split(' ')
console.log(saludoDividido)

//Para acceder a las posiciones del texto dividido
console.log(saludoDividido[1])

//Si se quiere eliminar los espacios de más
const saludoConEspacios = ' Hola mundo '
const saludoSinEspacios = saludoConEspacios.trim()
console.log(saludoSinEspacios)

//Si se quiere reemplazar alguno de los caracteres
const saludoOriginal = 'Hola mundo'
const nuevoSaludo = saludoOriginal.replace('Mundo', '🩷')
console.log(nuevoSaludo)