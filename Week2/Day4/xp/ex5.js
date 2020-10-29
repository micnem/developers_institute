let amazonBasket = {
    glasses: 1,
    books: 2,
    floss: 100
}

function checkBasket(item){
        if(item in amazonBasket){
            console.log("this item is in your basket")
        }
        else{
            console.log("this item is not in your basket")
        }
}
checkBasket("floss")

// console.log(Object.keys(amazonBasket))