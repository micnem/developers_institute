var tries = 3;
var userNumber = 0;
var computerNumber = 1; 

function playTheGame(){
    
    if(confirm("Confirm you want to play!") == false){
        alert("No problem. Goodbye!")
    }
    else{
        userNumber = prompt("Enter a number between 1-10", 4);
        if(isNaN(userNumber)|| userNumber>10){
            alert("An invalid input was entered. Goodbye.");
        }
        else{
            computerNumber = Math.floor(Math.random() * 11);
            console.log(computerNumber);
        }

    }
}

function test(userNumber, computerNumber){
    while(tries>0){
        if(userNumber == computerNumber){
            alert("Congratulations! You have won in ", tries," tries")
            
        }
        else if(userNumber > computerNumber){
            tries = tries -1;
            prompt("Your number was bigger, input another number. You have ", tries, " left");
            console.log(tries, " left");
        }
        else if (userNumber < computerNumber){
            tries = tries -1;
            prompt("Your number was smaller, input another number. You have ", tries, " left");
            console.log(tries, " left");
        }
}
    if(tries == 0){
        alert("game over")
    }
}

playTheGame();
test(userNumber, computerNumber)