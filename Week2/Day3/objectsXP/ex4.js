let Person1 = {
    firstName: "Jack",
    height: 1.80,
    mass: 100,
    BMI : function() {
        return this.mass / this.height**2;
      }
}
let Person2 = {
    firstName: "Michael",
    height: 1.88,
    mass: 85,
    BMI : function() {
        return this.mass / this.height**2;
      }
}


console.log(Person1.BMI())
console.log(Person2.BMI())