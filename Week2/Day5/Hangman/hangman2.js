function hangman(){

var input = prompt("User1. Type in a word.")
var wordStar = [];
var lives = 10;
var find = false;
var wrongLetters = [];
var remainingLetters = input.length;

for(var i = 0; i < input.length; i++){
	wordStar[i]= "*";
}

console.log(wordStar)

while(lives>0){
	var guess = prompt("User2, input a letter")
	find == false;
//correct
if(input.includes(guess)){
	for(var j = 0; j<input.length; j++){
		if(guess == input[j]){
			wordStar[j]=guess
			remainingLetters=remainingLetters-1
			find == true;
		}
	}
	console.log("correct! You have ",lives," left to guess ", wordStar)
}
//incorrect
else if(input.includes(guess)== false){
	lives = lives-1;
	wrongLetters.push(guess)
	console.log("Wrong, lives remaining: ", lives, " your incorrect guesses are ", wrongLetters)

}
//empty or too many characters entered
else if(guess==null){
	console.log("nothing was entered, please try again.")
}
else if(guess.length!==1){
	console.log("ONE LETTER PLEASE")
}
//repeated
else if (
      wrongLetters.includes(guess) == true ||
      wordstar.includes(guess) == true) {
      
      console.log(
        "You already guessed that letter! Remaining guesses " + lives
      );
      find == false; 
    }

//game over
}

if(remainingLetters==0){
	find==false
	console.log("Well done! You are the winner! the word was ", input)
}
else if(lives<1){
	console.log("Game over. The word was ", input)
}
}

hangman()