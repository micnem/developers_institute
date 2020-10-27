let people = ["Greg", "Mary", "Devon", "James"]
var last = people[people.length -1]
console.log(last)

console.log(people.indexOf("Mary"))
console.log(people.indexOf("Foo"))

for(let i = 0; i<people.length; i++){
    console.log(people[i]);
}

people.splice(0,1)
people.splice(3,0,"Michael");

let i = 0;
do {
  console.log(people[i])
  i++;
}
while (i<1);

var newpeople = people.slice(1,3); 
console.log(newpeople); 


