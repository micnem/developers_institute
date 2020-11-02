let firstUl = document.querySelector("ul")
firstUl.lastElementChild.innerHTML = "Richard"

let secondUl = document.querySelectorAll("ul")[1];

let myName = document.querySelector("ul")
myName.firstElementChild.innerHTML = "Michael"

let newItem = document.createElement("li")
let hey = document.createTextNode("Hey Students!")
firstUl.appendChild(hey)

let newItem2 = document.createElement("li")
let hey0 = document.createTextNode("Hey Students!")
secondUl.appendChild(hey0)

let sarah = secondUl.children[1];
sarah.remove();