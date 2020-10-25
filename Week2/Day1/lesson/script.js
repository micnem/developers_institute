
//alert('Isaac');

//console.log('My Javascript file is connected');






//VARIABLES


//var name = 'Isaac';

//alert(name);

//console.log(name);



// var x;

// x = 3;

// console.log(x);



// var x, y;

// x = 5 + 6;

// y = x * 10;

// console.log(y);




//COMMENTS

 //var x = 5;   // I will be executed
// //var x = 6;  // I will NOT be executed


//console.log(x);


//ALERT

//alert(message);   Syntax

//alert("Hello");  //this will run first

//console.log('Hi there!')   //this will continue after the alert



//PROMPT

// var isaac = prompt('input');

// console.log(isaac);


// //`var result = prompt(title, [default])
//     //  title : the text to show the visitor.
//     // default: optional second parameter, the initial value for the input field.
//     var age = prompt('How old are you?', 30);
//    // alert(`You are ${age} years old!`); // You are 20 years old!

//     alert('You are ' + age + ' years old!'); // You are 20 years old!



//CONFIRM

// //var result = confirm(question);   //syntax

// var isBoss = confirm("Are you the boss?");

// alert( isBoss ); // true if OK is pressed






// STRINGS

//var text = 'Hello, Im a text';
//var text = "Hello, I'm a text";
//var text = 'Hello, I\'m a text';

//console.log(text);



// var child = 'Isaac';

// //console.log(child);



// var longString = "This is a very long string which needs " +
//                  "to wrap across multiple lines because " +
//                  "otherwise my code is unreadable.";




//var longString = "This is a very long string which needs to wrap across multiple lines because otherwise my code is unreadable. ";
                 

//console.log(longString);


// let longString = "This is a very long string which needs \
// to wrap across multiple lines because \
// otherwise my code is unreadable.";

// console.log(longString);





// NUMERIC

// var number = 23;

// var decimal = 23.5;


// console.log(number);

// console.log(decimal);



// BOOLEAN

// var boolean1 = true;

// var boolean2 = false;


// console.log(boolean1);




// ARRAYS


//syntax: var array = [];

// var child = 'Isaac';

// var family = ['Tali', 'Guillermo', 40, child, true];

// console.log(family);



// OBJECTS

//syntax: var obj = {};

// var plant = {

// 	color: 'green', 
// 	size: 'big', 
// 	quantity: 3
// }

// console.log(plant);

// var array = [];

// array = [plant, 'hello', 20, false];

// console.log(array);



// FUNCTIONS

// var myFunction = function(){

//     alert('Hiiiiiii');
// };


// myFunction();



// HTML ELEMENTS
// var header = document.querySelector('h1');

// console.log(header);


//STRINGS

// STRING OPERATORS

// var text1 = 'Hello';
// var text2 = ' How are you?';
// var number = 5;

// // + Concatenate

// var newText = text1 + text2 + ' ' + number;

// console.log(newText);

////////////////////////////////////////////////////////


// var text = 'Hello, I am a text';

// //length - The number of characters

// var numberCharacters = text.length;

// console.log(numberCharacters);


// let longString = "This is a very long string which needs \
// to wrap across multiple lines because \
// otherwise my code is unreadable.";

// var length_txt = longString.length;


// console.log(length_txt);






// toUpperCase() - Transform all characters to uppercase

// var text = 'Hello, I am a text';

// var upper = text.toUpperCase();

// console.log(upper);




// toLowerCase() - Transform all characters to lowercase

// var text = 'HELLO, I AM A TEXT';

// var lower = text.toLowerCase();

// console.log(lower);




// substring(0,0) - Extract from one point to another character

// var text = 'Hello, I am a text';

// var extract = text.substring(6, 9);

// console.log(extract);




// replace(value1, value2) - Replace one character string with another

// var text = 'Hello, I am a text';

// var textReplaced = text.replace('text', 'man');

// console.log(textReplaced);



// indexOf('o') - It will look for the first character that matches and will indicate the position

// var text = 'Hello, I am a text';

// var searchO = text.indexOf('o');

// console.log(searchO);


//Example 2
// var str = "hello Everyone, please say hello to the class ";
// var pos = str.indexOf("hello"); // pos = 0

// console.log(pos);



// lastIndexOf('o') - It will look for the last character that matches and will indicate the position

// var text = 'Hello, I am a texto';

// var searchLastO = text.lastIndexOf('o');

// console.log(searchLastO);


// split(' ') - The text string is converted into an array dividing the elements according to the specified separator

// var text = 'Hello, I am a texto';

// var array = text.split(' ');

// console.log(array);



//SUBSTRING

//var str = "Hello Everyone, please say hello to the class ";

// //var sub1 = str.substring(0,4) //returns "hell"


// var sub1 = str.substring(0,1) //returns "H"

// console.log(sub1);



// var sub2 = str.substring(3,6) //returns "lo"

// console.log(sub2);




//NUMBERS

// ARITHMETIC OPERATORS

// var firstNumber = 21;

// var secondNumber = 4;


// // // // + Sum

// var result = firstNumber + secondNumber;

// console.log(result);




 // - Subtraction

//  var firstNumber = 21;

//  var secondNumber = 4;

//  var result = firstNumber - secondNumber;

//  console.log(result);



 // * Multiplication

//  var firstNumber = 21;

//  var secondNumber = 4;

//  var result = firstNumber * secondNumber;

//  console.log(result);



 // / Division

//  var firstNumber = 21;

//  var secondNumber = 4;

// var result = firstNumber / secondNumber;

// console.log(result);




// % Module   //returns the remainder

// var firstNumber = 21;

//  var secondNumber = 4;

// var result = firstNumber % secondNumber;

// console.log(result);



// ++ Increment

// var firstNumber = 21;

//  var secondNumber = 4;

//  //var result = ++firstNumber;

//  var result = firstNumber + 1;

//  console.log(result);



 // -- Decrement

//   var firstNumber = 21;

//   var secondNumber = 4;

//  //var result = --firstNumber;

//  var result = firstNumber - 1;

//  console.log(result);




// ASSIGNMENT OPERATORS

// var number;

// // = Assign a value

// number = 5;

// console.log(number);



// += Assign a value by adding it with its previous

// var number;

// number = 5;

// number += 3;

// //number = number + 3;

// console.log(number);



// -= Assign a value by subtracting it with its previous

//  var number;

// number = 5;

// ///number -= 3;

// number = number - 3;

// console.log(number);



// *= Assign a value by multiplying it with its previous

// var number;

// number = 5;


// //number *= 3;

// number = number * 3;

// console.log(number);



// /= Assign a value by dividing it with its previous

// var number;

// number = 5;

// //number /= 3;

// number = number / 3;


// console.log(number);




// COMPARISON OPERATORS

// var number1 = 10;
// var number2 = 10;

// // == Equal to

// var result = number1 == number2;

// console.log(result);


//STRICT COMPARISON: STRING WITH NUMBER


// var number1 = 10;
// var number2 = '10';

// // == Equal to

// var result = number1 === number2;

// console.log(result);



// === Equal value and type

//  var number1 = 10;
//  var number2 = 10;

//  var result = number1 === number2;

//  console.log(result);




 // != Not equal to (Different)

//  var number1 = 10;
//  //var number2 = 10;

//  var number2 = '10';

//  var result = number1 != number2;

//  console.log(result);



 // !== Not equal to or in type


//  var number1 = 10;
//  var number2 = 10;

// var result = number1 !== number2;

// console.log(result);



// > greater than

// var number1 = 10;
// var number2 = 10;

// var result = number1 > number2;

// console.log(result);



// < less than

//  var number1 = 10;
//  var number2 = 10;

//  var result = number1 < number2;

//  console.log(result);




 // >= greater than or equal to

//  var number1 = 10;
//  var number2 = 10;

// var result = number1 >= number2;

// console.log(result);




// <= less than or equal to

// var number1 = 10;
// var number2 = 10;

// var result = number1 <= number2;

// console.log(result);




// LOGICAL OPERATORS

// &&    and

// ||    or

// !     no / negation



//&&

// var number1 = 10;
// var number2 = 9;

// var result = (number1 && number2) === 10;

// console.log(result);



//OR ||


// var number1 = 1;
// var number2 = 9;

// var result = (number1 || number2) === 10;

// console.log(result);




//!     no / negation

// var number1 = 10;
// var number2 = 10;

// var result = !(number1 || number2) === 10;

// console.log(result);


// var negation = true;

// negation = false;

// console.log(!negation);




//NUMBER AND SRING METHODS

//var op = 10/"me";

//console.log(op)


//isNaN(op);   //returns true because op is Not a Number


//console.log(isNaN(op));



//The toString() method: returns a number as a string.

//var op = 10;

//console.log(op);

//op.toString();     //returns "10"

//console.log(op.toString());



//The toFixed() method: returns a string, with the number written with a specified number of decimals

//var op = 10.6789;

//op.toFixed(0);           // returns 11

//console.log(op.toFixed(0));

//op.toFixed(2);           // returns 10.68.

//console.log(op.toFixed(2));



//Boolean
//JavaScript has a Boolean data type. It can only take the values true or false

//The Boolean() method: to find out if an expression (or a variable) is true

//var op = Boolean(10 > 9)   // op returns true

// var op = (10 > 9) 

// console.log(op);





//ARRAYS

 //var family = ['Tali', 'Lea', 'William', 'Dov', 'Shai', 'Rafi', 'Isaac'];

 //console.log(family[2], family[3] );

 //console.log(family[0].toString().split('')[3]);







// var family = [];

// family[0] = 'Dov';
// family[1] = 'William';
// family[2] = 'Tali';
// family[3] = 'Shai'

// console.log(family);




// METHODS AND PROPERTIES FOR ARRAYS

// var family = ['Tali', 'William', 'Dov'];

// var familyTwo = ['Shai', 'Rafi'];

// // length  //Returns the number of elements in the array

// var quantityElementsFamily = family.length;

// var quantityElementsFamily2 = familyTwo.length;

// console.log(quantityElementsFamily);

// console.log(quantityElementsFamily2);




// Join	// Join the arrays

// var family = ['Tali', 'William', 'Dov'];

// var familyTwo = ['Isaac', 'David'];

//join    // Contrary to split - Show all elements of the array in a text string

// var text = family.join('-');

// console.log(text);


// concat	// Concatenates the arrays


//  var newFamily = family.concat(familyTwo);

//  console.log(newFamily);





// pop	// Delete the last element of the array

// var family = ['Tali', 'Dov', 'William'];

// //family.pop();

// console.log(family.pop());

// console.log(family);



// push	// Add an element to the end of the array

// var family = ['Tali', 'Dov'];

// family.push('William');

// //console.log(family.push('William'));

// console.log(family);



// shift	// Remove the first element of the array

// var family = ['Tali', 'Dov', 'William']

// family.shift();

// //console.log(family.shift());

// console.log(family);



// unshift	// Add an element to the beginning of the array

// var family = ['Tali', 'Dov']

// family.unshift('William');

// //console.log(family.unshift('Daniel'));

// console.log(family);




// reverse	// Order the array backwards

// var family = ['Rafi', 'Dov', 'Tali'];

// // family.reverse();

// console.log(family.reverse());




//TYPEOF


// console.log(typeof 42);
// // expected output: "number"

// console.log(typeof 'blubber');
// // expected output: "string"

// console.log(typeof true);
// // expected output: "boolean"

// console.log(typeof undeclaredVariable);
// // expected output: "undefined"


// var colors = ["blue", "yellow", "green"]; 

// console.log(colors);

// console.log(typeof colors) // object



//Changing an Array Element

// var colors = ["blue", "yellow", "green"];

// colors[0] = "pink"

// console.log(colors) // ["pink", "yellow", "green"]; 



//SPLICE METHOD

//syntax array.splice(index, howmany, item1, ....., itemX)

// var colors = ["blue", "yellow", "green" ]; 

// colors.splice(1, 1, 45, 23); // var colors = ["blue", 45, 23, "green" ]; 

// console.log(colors);



//SLICE

// var colors = ["blue", "yellow", "green", "pink" ]; 

// var favorite = colors.slice(2) // favorite = ["green" , "pink"]; 


// console.log(favorite);

// console.log(colors);


// var second_favorite = colors.slice(0,1) // favorite = ["blue"]; 

// console.log(second_favorite);

// console.log(colors);





//the toString() method: converts an array to a string of (comma separated) array values.

// var colors = ["blue", "yellow", "green" ]; 

// colors.toString() // blue,yellow,green

// console.log(colors.toString());



// OBJECT OR OOP ORIENTED PROGRAMMING


// It is a series of rules of doing things
// so that other people can use them
// and advance their work, so that we get
// that the code can be reused.

// CLASSES

// OBJETS



// CLASSES
// They are functions, called constructor functions and are written starting with Uppercase

// JAVASCRIPT CLASSES

//  var text = new String("Hi i'm a text");

//  var num = new Number(5);

//  var bool = new Boolean(true);



//  // COMPOSITE JAVASCRIPT CLASSES

//  var arrays = new Array('Alejandro', 'Maria', 'Pedro');

//  var obj = new Object({color: 'green', size: 'big'});


 // PERSONALIZED CLASSES

//  function Person(name, age){

// 	this.name = name;
// 	this.age = age;

// }


//  var person1 = new Person();
//  person1.name = 'Isaac';
//  person1.age = 50;

//  console.log(person1);


//  var person2 = new Person();
//  person2.name = 'Roy';
//  person2.age = 20;

//  //console.log(person2);

//  console.log(Person());


// OBJETS
// It is a collection of properties and methods


// var plant = {

// 	color: 'green',
//     size: 'big',
    
// 	writeInformation: function(price){
// 		console.log('The color of the plant is ' + plant.color + ' and its size is ' + plant.size + ', and its price is ' + price);
// 	}

// }

// //console.log(plant);

// //console.log(plant.color);

// //console.log(plant.size);

// plant.writeInformation('$1500');


// var person = {

//     firstName: "John",

//     lastName: "Doe",

//     age: 50,

//     eyeColor: "blue"

//   };

//console.log('His name is ' + person.firstName + ' and his last name is ' + person.lastName);

//console.log('His age is ' + person.age);



//Adding/ Changing Object properties

// var person = {

//   firstName: "John",

//   lastName: "Doe",
// };

// person.firstName = "Sarah"

// person.eye_color= "blue"

// console.log(person)



// var person = {

//     firstName: "John",

//     lastName: "Doe",
//   };


//   delete person.firstName

//   console.log(person);




// var array = []

// console.log(typeof array);






//RANDOM METHODS

// Get random numbers
// Math.random();

//var random = Math.random() * 1000;
//console.log(random);


//var randomNumber = Math.round(Math.random()*1000);
//console.log(randomNumber);


// Round to the smallest whole number                                        Redondear al número entero menor
//var randomNumber2 = Math.floor(Math.random()*10)
//console.log(randomNumber2);

// Round to the largest whole number
//var randomNumber3 =  Math.ceil(Math.random()*10)
//console.log(randomNumber3);

// Round to the nearest whole number
//var randomNumber4 =  Math.round(Math.random()*1000)
//console.log(randomNumber4);
