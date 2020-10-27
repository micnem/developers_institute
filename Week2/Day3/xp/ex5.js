var value = "123";
var sum = 0;


for (var i = 0; i < value.length; i++) {
    
    var test1 = parseInt(value[i]);
  
    sum += test1 
}


if(sum%3==0){
     console.log("divisible by three");
        }
else{console.log("not divisible by three")}
