//ejercicio

//user information

const username = "batman";
const fullName = "Bruce Wayne";
const age = 24;
const isStudent = true;


// address

const address = {
    street: "Gotham Street",
    city: "Gotham",
    state: "New York",
    zipCode: 123456789
};

// hobbies

const hobbies = ["fighting", "money", "justice"];


// Generateing personalized bio

const personalized = `My name is ${fullName}, I'm ${age} years old and I live in ${address.city}, ${address.state}. I like ${hobbies.join(", ")}. and i am ${username} and work in ${address.street}`;

//print the user information
console.log(personalized);