// Funciones Constructoras en JavaScript
// Las funciones constructoras en JavaScript se utilizan para crear objetos con propiedades y métodos específicos. 
// Sirven como un modelo para definir el comportamiento y las características de los objetos. Cuando se llama a una función 
// constructora con la palabra clave new, se crea un nuevo objeto y se ejecuta el código de la función constructora. Este 
// nuevo objeto hereda las propiedades y métodos definidos dentro de la función constructora.

// Función para definir un mensaje personalizado
const mensajePersonalizado = () => '¡Adiós a todos!';

// Función constructora para crear objetos Cohete
function Cohete(nombre, mensajeLanzamiento) {
  // Establecer las propiedades del objeto usando la palabra clave 'this'
  this.nombre = nombre;
  this.mensajeLanzamiento = mensajeLanzamiento;
}

// Crear dos objetos Cohete usando la función constructora
const coheteFalcon9 = new Cohete('Falcon 9', mensajePersonalizado);
const coheteFalconHeavy = new Cohete('Falcon Heavy', mensajePersonalizado);

// Acceder a las propiedades del objeto y llamar a los métodos
console.log(coheteFalcon9.nombre);  // Salida: "Falcon 9"
console.log(coheteFalcon9.mensajeLanzamiento());  // Salida: "¡Adiós a todos!"

// Crear objetos Cohete usando una función flecha (enfoque alternativo)
const CoheteConFuncionFlecha = (nombre, mensajeLanzamiento) => ({
  nombre: nombre,
  mensajeLanzamiento: mensajeLanzamiento
});

// Definir un mensaje personalizado para la función flecha
const mensajePersonalizadoParaFuncionFlecha = () => '¡Lanzamiento exitoso!';

// Crear un objeto Cohete usando la función flecha
const coheteFalcon9_1 = CoheteConFuncionFlecha('Falcon 9', mensajePersonalizadoParaFuncionFlecha);

// Acceder a las propiedades del objeto (sintaxis alternativa para objetos de función flecha)
console.group(coheteFalcon9_1.nombre);  // Salida: "Falcon 9"
console.group(coheteFalcon9_1.mensajeLanzamiento());  // Salida: "¡Lanzamiento exitoso!"



// DESVENTAJAS DE DUPLICAR CODIGO

// Mantenimiento difícil: Duplicar código hace que mantener y actualizar el software sea más complicado. Cuando se realiza 
// un cambio en una parte del código duplicado, es necesario recordar y aplicar ese cambio en todas las instancias duplicadas, 
// lo que puede ser propenso a olvidos y errores.

// Aumento de complejidad: La presencia de código duplicado aumenta la complejidad del sistema. En lugar de tener una única 
// fuente de verdad para una funcionalidad o lógica, hay múltiples instancias que deben ser coordinadas y gestionadas, lo que 
// puede resultar en un código más difícil de entender y mantener.

// Mayor probabilidad de errores: Duplicar código incrementa la posibilidad de introducir errores, ya que cualquier cambio 
// realizado en una instancia duplicada puede no propagarse de manera consistente a todas las demás. Esto puede conducir a 
// comportamientos inesperados y a la necesidad de corregir errores en múltiples lugares.

// Dificultad de escalar: A medida que el proyecto crece, la duplicación de código puede volverse más difícil de manejar. 
// La cantidad de código duplicado puede aumentar exponencialmente, lo que dificulta la adición de nuevas funcionalidades, 
// la corrección de errores y la mejora del sistema en general.

// Tiempo y recursos: Duplicar código implica utilizar más tiempo y recursos en el desarrollo y mantenimiento del software. 
// En lugar de reutilizar y mantener una única implementación, se deben dedicar recursos adicionales a mantener y sincronizar 
// múltiples copias del mismo código.

// Violación de principios de diseño (DRY): DRY (Don't Repeat Yourself) es un principio de diseño que aboga por la eliminación 
// de duplicación en el código. Duplicar código va en contra de este principio, ya que implica repetir la misma lógica en 
// varios lugares, lo cual es considerado una mala práctica de programación.

// Dificultad en la identificación de errores: Identificar y corregir errores se vuelve más desafiante cuando el código 
// está duplicado. La propagación de cambios puede no ser evidente de inmediato, lo que dificulta la tarea de encontrar y 
// corregir problemas en el software.

// Duplicación de código
function calcularAreaCuadradoLadoA(lado) {
    return lado * lado;
}

// ... algún código intermedio ...

function calcularAreaCuadradoLadoB(lado) {
    return lado * lado;
}

// Sin duplicación de código
function calcularAreaCuadrado(lado) {
    return lado * lado;
}

// ... algún código intermedio ...

// Se utiliza la función en diferentes lugares
let areaA = calcularAreaCuadrado(ladoA);
let areaB = calcularAreaCuadrado(ladoB);