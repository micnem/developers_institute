var number = 99;
var str1 = "bottles of beer on the wall";
var str2 = "bottles of beer";
var str3 = "take ";
var str4 = "down pass it around";

for(var i = 1; number>i; i++){
    number -= i;
    console.log(number, str1, number, str2, str3, i, str4, number - i, str1);
    
}

if (i>number){
    number =- number;
}

