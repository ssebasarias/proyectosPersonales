// fucio que recibe un numero y devuelte el numeor reorganizado de forma decendente
function ordenarNumero (num) {
    const digitos = obtenerDigitos(num)

    // Ordenamiento manual decendente
    for (let i = 0; i < digitos.length - 1; i ++) {
      for (let j = i + 1; j < digitos.length; j++) {
        if (digitos[i] < digitos[j]){
          const aux = digitos[i]
          digitos[i] = digitos[j]
          digitos[j] = aux
        }
      }
    }

    // Alternativa orden decendente
    // digitos.sort((a, b) => b - a);

    const numeroString = digitos.join("");
    const numeroEntero = parseInt(numeroString);
    return numeroEntero
} 

function obtenerDigitos (num) {
    const cadena = String(num)
     const  digitos = []
    for (let i = 0; i < cadena.length; i++){
        digitos.push(cadena[i])
    }

    return digitos
}

// Alternativa para ordenar


const numeroEjemplo = 12345;
const digitos = obtenerDigitos(numeroEjemplo);
console.log(digitos); // Salida: ["1", "2", "3", "4", "5"]

const ordenado = ordenarNumero(numeroEjemplo);
console.log(ordenado); // Salida: 54321
