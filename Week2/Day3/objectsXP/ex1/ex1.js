var input = prompt("what is your name?")
let guestList = {
    Randy: "Germany",
    Karla: "France",
    Wendy: "Japan",
    Norman: "England",
    Sam: "Argentina"
  }
  if(guestList[input] == undefined){
      console.log("Welcome guest!")
  }
  else{console.log(guestList[input])}

