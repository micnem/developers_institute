var input = prompt("User1, enter your word")
var inputArr = [];
var newArr = []
var guess = prompt("guess a letter")
var remLet = input.length
var wrongLet = [];
var corLet = [];
var lives = 10;

if(input.length<4){
	var input = prompt("input is less than 4 characters, try again.")
}
else{
	for(var i = 0; i<input.length;i++){
	inputArr.splice(i, i,"*") 
	}
	newArr.push(inputArr)
}
console.log(newArr)

while(lives>0){
	if(input.includes(guess)){ //correct
		for(var j = 0; j<inputArr.length; j++){
			inputArr[j]=guess
			remLet = remLet -1
			console.log("correct!", inputArr)
			guess = prompt("input another number")
	}
		}
	else if(input.includes(guess)==false){//incorrect
		wrongLet.push(guess)
		lives = lives-1
		console.log("Wrong! you have ", lives, " lives remaining" ,wrongLet)
		guess = prompt("input another number")
	}
	else if(guess.length!==1){//incorrect input
		console.log("only one letter")
	}
	else if(lives==0){
		console.log("You lose, game over")
		break;
	}
}
// else{
// 	console.log("incorrect!")
// 	}


	

