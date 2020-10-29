let age = 19
let canDrive = false;
if (age > 18) {
    console.log(age) // 20
    let canDrive = true 
    console.log(canDrive); // true
} 
console.log(canDrive); //ReferenceError: canDrive is not defined