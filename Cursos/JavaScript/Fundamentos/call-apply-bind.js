// - Método apply 📌
// ✅ Concepto: apply() es una función en JavaScript que se utiliza para llamar a otra función con un valor específico para this y un array (o un objeto similar a un array) de argumentos.


funcion.apply(thisArg, [argsArray])

// funcion: La función a la que se llamará.
// thisArg: El valor que será utilizado como this dentro de la función.
// argsArray: Un array o un objeto similar a un array que contiene los argumentos que se pasarán a la función.
// Ejemplo🔎

function saludar(nombre, saludo) {
  console.log(`${saludo}, ${nombre}!`);
}

const persona1 = {
  nombre: 'Ana'
};

// Usando apply para llamar a la función con un array de argumentos
saludar.apply(persona1, ['Hola', 'Señorita']);


// - Método call 📌
// ✅ Concepto: call() es un método que se utiliza para invocar (llamar) a otra función con un valor específico para this (el contexto de ejecución) y con argumentos proporcionados de forma individual.


//funcion.call(thisArg, arg1, arg2, ...);

// funcion: La función que se va a llamar.
// thisArg: El valor que se asignará como this cuando la función sea llamada.
// arg1, arg2, ...: Argumentos individuales que se pasarán a la función.
// Ejemplo🔎

const persona2 = {
  nombre: 'Juan',
  saludar: function(saludo) {
    console.log(`${saludo}, soy ${this.nombre}.`);
  }
};

const otraPersona = {
  nombre: 'Maria'
};

// Llamando a la función saludar de persona con el contexto de otraPersona
persona2.saludar.call(otraPersona, 'Hola'); 
// Imprime: Hola, soy Maria.


// - Método bind 📌
// ✅ Concepto: bind() crea una nueva función, que cuando es llamada, asigna a su operador this el valor entregado, con una secuencia de argumentos dados precediendo a cualquiera entregados cuando la función es llamada.


//funcionOriginal.bind(thisArg[, arg1[, arg2[, ...]]]);

// funcionOriginal: La función original que se va a llamar.
// thisArg: El valor que se asignará como this cuando la nueva función sea llamada.
// arg1, arg2, ...: Argumentos opcionales que se predefinirán para la nueva función.
// Ejemplo🔎

const persona3 = {
  nombre: 'Juan',
  saludar: function() {
    console.log(`Hola, soy ${this.nombre}.`);
  }
};

const saludarJuan = persona3.saludar.bind(persona3);
saludarJuan(); // Imprime: Hola, soy Juan.