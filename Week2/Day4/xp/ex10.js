function hotel_cost(){
    var price = 0;
    var input = 4;
        if(input==NaN){
            prompt("Not valid. try again.")
        }
        else{
            price += input*140;
            return price
        }
}

console.log(hotel_cost())

function plane_ride_cost(){ 
    var fare = 0;
    var input = "Paris";
        if(input == "London"){
            return(183)
        }
        else if (input == "Paris"){
            return(220)
        }
        else if (typeof input !== "string"){
            return("invalid input. try again.")
        }
        else {
            return(300)
        }
}
console.log(plane_ride_cost());

function rental_car_cost(){
    var price = 0;
    var input = 4;
        if(input==NaN){
            prompt("Not valid. try again.")
        }
        else{
            price += input*40;
            return price;
        }
}
console.log(rental_car_cost())

function total_vacation_cost(){
    var totalCost = rental_car_cost() + plane_ride_cost() + hotel_cost() 
    return totalCost; 
}

console.log(total_vacation_cost())