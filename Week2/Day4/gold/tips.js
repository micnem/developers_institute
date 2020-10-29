// var input = prompt("type in tip amounts seperated by commas");
var arr = [20, 60, 220]
// input.split("");
var tipArray = [];
var total = [];



function tipCalc(){
    arr.forEach(i => {
    
        if(i<50){
            tipArray.push(i * 0.2);
            total.push(i + (i * 0.2));
    
        }
        else if(i>50&&i<200){
            tipArray.push(i * 0.15);
            total.push(i + (i * 0.15));
        }
        else{
            tipArray.push(i * 0.1);
            total.push(i + (i * 0.1));
        }
    }
    );
    
    console.log(tipArray);
    console.log(total);

}
tipCalc();






