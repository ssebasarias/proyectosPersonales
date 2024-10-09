// Enlace Implícito:


const house = {
    dogName: 'Sheldon',
    dogGreeting: function() {
        console.log(`Hi, my name is ${this.dogName}`);
    }
}

house.dogGreeting(); // Salida: Hi, my name is Sheldon
// En este ejemplo, la función dogGreeting está definida como un método dentro del objeto house.
// Cuando se llama a house.dogGreeting(), this en la función hace referencia al objeto house, ya que es el objeto que contiene y llama al método. Enlace Explícito:

function dogGreeting() {
    console.log(`Hi, my name is ${this.dogName}`);
}

const newHouse = {
    dogName: 'Scannor',
}

dogGreeting.call(newHouse); // Salida: Hi, my name is Scannor
// En este caso, la función dogGreeting se define de manera independiente.
// Se utiliza el método call para cambiar explícitamente el valor de this en la función dogGreeting a newHouse.
// this.dogName ahora hace referencia a Scannor, que es el valor de dogName en el objeto newHouse. Uso de call con Parámetros:

function newDogGreeting(owner, address) {
    console.log(`Hi, my name is ${this.dogName} and my owner is ${owner} and I live in ${address}`);
}

const owner = 'Beder';
const address = 'Calle 123';

newDogGreeting.call(newHouse, owner, address);
// Salida: Hi, my name is Scannor and my owner is Beder and I live in Calle 123
// En este ejemplo, la función newDogGreeting tiene dos parámetros (owner y address).
// call se utiliza para cambiar this a newHouse y pasar los valores de owner y address como argumentos a la función.