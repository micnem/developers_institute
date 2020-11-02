// Get the div DOM node

// method 1 
console.log(document.querySelector("div"));
// method 2
console.log(document.getElementsByTagName("div")[0]);

// Get the The ul DOM node

// method 1

var x = document.querySelector("ul");
console.log(x)

// method 2
console.log(document.getElementsByTagName("ul")[0]);


// Get the second li (with Pete)
// Method 1
var ul = document.querySelector("ul")
var name1 = ul.children[1]
console.log(name1)

// Method 2

