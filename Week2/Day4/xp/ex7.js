let shoppingList=["banana", "apple", "orange"] 

let stock = { 
    "banana": 6, 
    "apple": 0,
    "pear": 12,
    "orange": 32,
    "blueberry":1
}  

let prices = {    
    "banana": 4, 
    "apple": 2, 
    "pear": 1,
    "orange": 1.5,
    "blueberry":10
} 

function myBill(){
    var sum = 0;

    for(item of shoppingList){
        if(stock[item] > 0){
            sum += prices[item];
            stock[item]--;
        }
    }
    return sum;
}

console.log(myBill());
console.log(stock)
