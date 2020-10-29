var input = prompt("what is your name?")
let guestList = {
    Randy: "Germany",
    Karla: "France",
    Wendy: "Japan",
    Norman: "England",
    Sam: "Argentina"
  }
  if(input in guestList){
    console.log("Hi! I'm  " + input + " from " + guestList[input]);
  }
  else{console.log("Welcome guest!")}    

