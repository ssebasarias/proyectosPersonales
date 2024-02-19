const saludoBienvenida = 'Hola mundo'
let operacionSimple = 1

let resultado = operacionSimple + 2
print(resultado)

// Al parecer n9o es necesario poner ";" siempre y cuando este bien identado, pero creo que es buena practica ponerlo 

// ============== VARIABLES PRIMITVAS
// inmutables, es decir, no se puede cambiar el valor original (para combinar datos se necesita de una conversion)
String 
Number 
Boolean
null
undefined
Symbol
BigInt

// ============== VARIABLES COMPLEJAS
// mutable, es decir, se puede cambiar el valor original (se pueden tener varios tipos de datos dentro de ellas)
Object
Array
function nomnbreFuncion (parametro) {};

// Object
let usuario = {
nombre: 'pepito',
edad: 13
}
usuario.edad = 20 // modifica un dato especifico dentro del objeto llamando el atributo especifico del objeto con el punto .
console.log(usuario)

// Array
let frutas = ["sandias","bananos"]
frutas[0] = "manzanas" // modifica el dato en la posicion especificada, en este caso el primer objeto
console.log(frutas)

// function
function cambiarNombre (objeto) {
objeto.nombre = 'Nuevo nombre'
};
let persona = {nombre:'Antonio'}

cambiarNombre(persona) // Asi se llama la funcion ( se esta cambiando el atributo nombre del objeto persona)